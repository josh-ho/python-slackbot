import requests
from flask import Flask, jsonify, request
from slackbot.slack import Slack

def configure_routes(app):
	slack = Slack()

	@app.route("/webhook", methods = ['POST'])
	def home():
		if slack.verifyRequest(request):
			print("Message is from Slack")
			return okResponse()
		else:
			print("Message is not from Slack")
			return invalidResponse()
		return invalidResponse()

	@app.route("/testPost/<channelID>", methods = ['GET']) # "C020RBV28P2"
	def testPost(channelID):
		blocks=[
			{
				"type": "section",
				"text": {
					"type": "plain_text",
					"text": "This is a plain text section block via slackbot.",
					"emoji": True
				}
			},
			{
				"type": "actions",
				"elements": [
					{
						"type": "button",
						"text": {
							"type": "plain_text",
							"text": "Click This Button",
							"emoji": True
						},
						"value": "selected-button-1",
						"action_id": "actionId-0"
					}
				]
			}
		]

		slack.postMessage(
			channelID, 
			"Hello from Slackbot", 
			blocks
		)
		return okResponse()

	@app.route("/health")
	def health():
		return okResponse()

	def okResponse():
		resp = jsonify(success=True)
		resp.status_code = 200
		return resp

	def invalidResponse():
		resp = jsonify(success=False)
		resp.status_code = 400
		return resp