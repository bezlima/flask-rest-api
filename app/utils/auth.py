from flask import current_app, jsonify
from jose import jwt, JWTError

def generate_jwt(payload):
    token = jwt.encode(payload, current_app.config.get('SECRET_KEY'), algorithm=current_app.config.get('ALGORITHM'))
    return token

def verify_jwt(token):
    try:
        payload = jwt.decode(token, current_app.config.get('SECRET_KEY'), algorithms=[current_app.config.get('ALGORITHM')])
        return payload
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired"}), 401
    except JWTError as e:
        return jsonify({"error": "Token is invalid"}), 401
