from flask import request, jsonify, Blueprint
from app.database.db import  db
from app.models.user_model import User
from app.utils.auth import verify_jwt

user_bp = Blueprint('user', __name__)

@user_bp.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    authorization = request.headers.get('Authorization')
    if not authorization:
        return "token is missing", 422
    hasToken = authorization.split(' ')
    if not len(hasToken) == 2:
        return "Token is missing", 422
    token = authorization.split(' ')[1]
    if not token:
        return "Token is missing", 422
    payload = verify_jwt(token)
    if not payload:
        return "Token is invalid", 422
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'username': user.username, 'email': user.email})

@user_bp.route("/user/edit/<int:user_id>", methods=["PATCH"])
def edit_user(user_id):
    authorization = request.headers.get('Authorization')
    if not authorization:
        return "Token is missing", 422
    hasToken = authorization.split(' ')
    if not len(hasToken) == 2:
        return "Token is missing", 422
    token = authorization.split(' ')[1]
    if not token:
        return "Token is missing", 422
    payload = verify_jwt(token)
    if isinstance(payload, tuple):  
        return payload  

    data = request.json
    email = data.get('email')
    username = data.get('username')
    new_password = data.get('password')

    if not email or not username or not new_password:
        return jsonify({"message": "Email, username, and password are required"}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    if user.email != email or user.username != username:
        return jsonify({"message": "Email or username does not match"}), 403

    user.password = new_password  
    db.session.commit()

    return jsonify({"message": "User updated successfully"})

@user_bp.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    authorization = request.headers.get('Authorization')
    if not authorization:
        return "token is missing", 422
    hasToken = authorization.split(' ')
    if not len(hasToken) == 2:
        return "Token is missing", 422
    token = authorization.split(' ')[1]
    if not token:
        return "Token is missing", 422
    payload = verify_jwt(token)
    if isinstance(payload, tuple): 
        return payload 

    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted successfully"})

@user_bp.route("/users", methods=["GET"])
def list_users():
    authorization = request.headers.get('Authorization')
    if not authorization:
        return jsonify({"error": "Token is missing"}), 422
    
    hasToken = authorization.split(' ')
    if len(hasToken) != 2:
        return jsonify({"error": "Token is missing"}), 422
    
    token = hasToken[1]
    if not token:
        return jsonify({"error": "Token is missing"}), 422
    
    payload = verify_jwt(token)
    if isinstance(payload, tuple): 
        return payload  

    users = User.query.all()
    if not users:
        return jsonify({"message": "No users found"}), 404

    result = [{'username': user.username, 'email': user.email} for user in users]
    return jsonify({"users": result})
