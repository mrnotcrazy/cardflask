from flask import Flask, render_template, request
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from decouple import config


import requests
import json
from random import choice
import string

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from core import routes
