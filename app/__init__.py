from flask import Flask
from .config.config import load_config
from .database.db import db
from .routes import register_blueprints
from .config.cli import register_commands

app = Flask(__name__)
load_config(app)

db.init_app(app)

register_blueprints(app)

register_commands(app)

