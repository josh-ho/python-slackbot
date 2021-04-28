import pytest
from dotenv import load_dotenv
from flask import Flask
from slackbot.handlers.routes import configure_routes

load_dotenv()

@pytest.fixture
def app():
    app = Flask(__name__)
    configure_routes(app)
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

