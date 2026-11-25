import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.0")

@app.route("/")
def home():
    return f"""
    <h1>Jenkins CI/CD Lab</h1>
    <p>Application Version: {APP_VERSION}</p>
    <p>Status: Running</p>
    """

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
