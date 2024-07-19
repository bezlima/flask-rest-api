from dynaconf import FlaskDynaconf

def load_config(app):
    app_settings = FlaskDynaconf(
        app,
        settings_files=["settings.toml", ".secrets.toml"],
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = app.config.get('MODIFICATIONS')
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config.get('DATABASE_URI')
    app.config['SECRET_KEY'] = app.config.get('SECRET_KEY')
