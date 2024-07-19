from flask.cli import with_appcontext
from app.database.db import db

@with_appcontext
def initialize_database():
    print("Creating tables...")
    db.create_all()
    print("Tables created.")

def register_commands(app):
    app.cli.command('init-db')(initialize_database)
