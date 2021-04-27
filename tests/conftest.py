import pytest
from app import app as slackbot_app

@pytest.fixture
def app():
    yield slackbot_app

@pytest.fixture
def client(app):
    return app.test_client()

