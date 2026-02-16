from flask import Flask, jsonify, request

app = Flask(__name__)
SECRET_TOKEN = "gold123"

@app.route("/vault")
def vault():
    token = request.headers.get("Authorization")
    if token != SECRET_TOKEN:
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify({"gold": "💰 You accessed the vault!"})

app.run(host="0.0.0.0", port=5000)
