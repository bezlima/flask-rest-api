from flask import request, jsonify, Blueprint
from datetime import datetime, timedelta, timezone
from app.models.user_model import User
from app.utils.auth import generate_jwt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if user:
        payload = {
            'sub': str(user.id),
            'exp': datetime.now(timezone.utc) + timedelta(minutes=30),
            'iat': datetime.now(timezone.utc)
        }
        token = generate_jwt(payload)
        return jsonify({"token": token})
    return "Invalid username or password", 401