from flask import Flask
from dotenv import load_dotenv
from slackbot.handlers.routes import configure_routes

load_dotenv()

app = Flask(__name__)

configure_routes(app)

if __name__ == '__main__':
    app.run(debug=True)