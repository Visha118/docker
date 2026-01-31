from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"service":"service-health-api","status":"running"})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "UP"})

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message":"Hello from Service Health API"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777)
