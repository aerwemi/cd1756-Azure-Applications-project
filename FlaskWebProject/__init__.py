"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
# 
# Add any logging levels and handlers with app.logger
# Get the Gunicorn error logger so Flask can reuse its handlers when running under Gunicorn.
gunicorn_logger = logging.getLogger('gunicorn.error')
# Attach Gunicorn's handlers to the Flask app logger so log messages appear in the same output.
app.logger.handlers = gunicorn_logger.handlers
# Set the Flask app logger level to INFO to capture informational and above messages.
app.logger.setLevel(logging.INFO)
# Create a stream handler that writes log messages to standard output / stderr.
streamHandler = logging.StreamHandler()
# Set the stream handler level to INFO as well.
streamHandler.setLevel(logging.INFO)
# Add the stream handler to the Flask app logger.
app.logger.addHandler(streamHandler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
