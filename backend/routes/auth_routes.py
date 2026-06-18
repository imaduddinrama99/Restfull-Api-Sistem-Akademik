from flask import Blueprint, request, jsonify
from services import auth_service

# Membuat blueprint khusus untuk auth
auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    try:
        payload = request.json
        email = payload.get("email")
        password = payload.get("password")
        
        auth_response = auth_service.login(email, password)
        token = auth_response.session.access_token
        
        return jsonify({
            "status": "success", 
            "message": "Login berhasil!",
            "token": token
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": "Email atau password salah!"}), 401