from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/RenderVideo")
def RenderVideo():
    path = request.args.get('path')
    return jsonify({"numFrames": 69, "frames": [], "test": "Test Passed"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)