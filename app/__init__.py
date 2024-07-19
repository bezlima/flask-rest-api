from flask import Flask, Blueprint
from .config.config import load_config
from .database.db import db
from .routes import register_blueprints
from .config.cli import register_commands

app = Flask(__name__)
load_config(app)

# Inicializar SQLAlchemy com a aplicação Flask
db.init_app(app)

# Registrar blueprints
register_blueprints(app)

# registrar comandos
register_commands(app)

