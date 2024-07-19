from .server import server_bp
from .user import user_bp
from .auth import auth_bp
from .register import register_bp

def register_blueprints(app):
    app.register_blueprint(server_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(register_bp)
