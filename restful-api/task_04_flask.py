#!/usr/bin/python3
"""Simple API built using the Flask framework."""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Başlanğıc olaraq nümunədə göstərilən istifadəçiləri daxil edirik
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@app.route("/")
def home():
    """Root endpoint that returns a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Returns a JSON list of all stored usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """Returns the operational status of the API."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Returns the full object for a given username or 404 if not found."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user to the dictionary with validations."""
    # force=True və silent=True həm xətalı JSON-u, həm də başlıqsız dataları tutur
    data = request.get_json(force=True, silent=True)

    if data is None or not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
