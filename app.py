from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

@app.route("/api/data")
def get_data():
    return jsonify({"message": "React에서 잘 받아옴!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
