import os
import time
import urllib
import hmac
import hashlib
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class Slack:
	def __init__(self):
		slackToken = os.getenv('SLACK_BOT_TOKEN')
		self.client = WebClient(token=slackToken)
		self.slackSigningSecret = bytes(os.getenv("SLACK_SIGNING_SECRET"), "utf-8")

	def postMessage(self, channel, message, blocks):
		try:
			response = self.client.chat_postMessage(
				channel=channel,
				text=message,
				blocks=blocks
			)
			return response
		except SlackApiError as e:
			# You will get a SlackApiError if "ok" is False
			assert e.response["ok"] is False
			assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
			print(f"Got an error: {e.response['error']}")

	def verifyRequest(self, request):
		requestBody = request.get_data().decode()
		timestamp = request.headers['X-Slack-Request-Timestamp']
		if (time.time() - int(timestamp)) > 60 * 5:
			# The request timestamp is more than five minutes from local time.
			# It could be a replay attack, so let's ignore it.
			return False
		
		basestring = f"v0:{timestamp}:{requestBody}".encode("utf-8")

		mySignature = (
			"v0=" + hmac.new(self.slackSigningSecret, basestring, hashlib.sha256).hexdigest()
		)

		slackSignature = request.headers['X-Slack-Signature']
		if hmac.compare_digest(mySignature, slackSignature):
			return True
		else:
			return False