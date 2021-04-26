# Slackbot

This is a simple Slackbot written in python designed to post block messages to your slack channel.  This application starts a Flask app running on port 5000 that can listen for Slack webhooks and post to a specific channel that the Slack bot has been invited to.

## Requirements
* Python 3.7+

## Setup
* Install the dependendcies
* Create a `.env` file on the root of the project containing 2 keys.  These keys can be found on your Slack's bot application [https://api.slack.com/apps](https://api.slack.com/apps):
	* SLACK_BOT_TOKEN
	* SLACK_SIGNING_SECRET


## Sending messages
This slackbot sends messages using the Slack block kit builder [https://app.slack.com/block-kit-builder](https://app.slack.com/block-kit-builder)