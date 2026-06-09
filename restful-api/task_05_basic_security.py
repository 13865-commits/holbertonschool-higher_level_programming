#!/usr/bin/python3
"""Flask API demonstrating Basic Auth, JWT Authentication, and RBAC."""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Təhlükəsizlik açarlarını təyin edirik
app.config["SECRET_KEY"] = "flask-api-secret-key-12345"
app.config["JWT_SECRET_KEY"] = "jwt-api-secret-key-67890"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Tapşırıq təlimatında tələb olunan ilkin istifadəçilər lüğəti
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# --- Basic Authentication Doğrulaması ---
@auth.verify_password
def verify_password(username, password):
    """Verifies the basic authentication credentials."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


# --- JWT Xüsusi Xəta Menecerləri (Mütləq 401 qaytarmalıdır) ---
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handles missing or invalid token errors."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handles invalid token errors."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handles expired token errors."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handles revoked token errors."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handles fresh token requirement errors."""
    return jsonify({"error": "Fresh token required"}), 401


# --- API Endpoints (Baxış Nöqtələri) ---

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Protected route using HTTP Basic Authentication."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Logs in a user and returns a JWT token if credentials are valid."""
    data = request.get_json(force=True, silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        # İstifadəçinin adını token-in kimliyi (identity) kimi təyin edirik
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token}), 200

    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Protected route using JWT Authentication."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Protected route restricted to users with the 'admin' role."""
    current_user = get_jwt_identity()
    user_info = users.get(current_user)

    # Rolun admin olub-olmadığını yoxlayırıq (Authorization addımı)
    if user_info and user_info.get("role") == "admin":
        return "Admin Access: Granted"

    return jsonify({"error": "Admin access required"}), 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)#!/usr/bin/python3
"""Flask API demonstrating Basic Auth, JWT Authentication, and RBAC."""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Təhlükəsizlik açarlarını təyin edirik
app.config["SECRET_KEY"] = "flask-api-secret-key-12345"
app.config["JWT_SECRET_KEY"] = "jwt-api-secret-key-67890"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Tapşırıq təlimatında tələb olunan ilkin istifadəçilər lüğəti
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# --- Basic Authentication Doğrulaması ---
@auth.verify_password
def verify_password(username, password):
    """Verifies the basic authentication credentials."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


# --- JWT Xüsusi Xəta Menecerləri (Mütləq 401 qaytarmalıdır) ---
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handles missing or invalid token errors."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handles invalid token errors."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handles expired token errors."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handles revoked token errors."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handles fresh token requirement errors."""
    return jsonify({"error": "Fresh token required"}), 401


# --- API Endpoints (Baxış Nöqtələri) ---

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Protected route using HTTP Basic Authentication."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Logs in a user and returns a JWT token if credentials are valid."""
    data = request.get_json(force=True, silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        # İstifadəçinin adını token-in kimliyi (identity) kimi təyin edirik
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token}), 200

    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Protected route using JWT Authentication."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Protected route restricted to users with the 'admin' role."""
    current_user = get_jwt_identity()
    user_info = users.get(current_user)

    # Rolun admin olub-olmadığını yoxlayırıq (Authorization addımı)
    if user_info and user_info.get("role") == "admin":
        return "Admin Access: Granted"

    return jsonify({"error": "Admin access required"}), 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
