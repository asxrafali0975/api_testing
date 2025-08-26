from flask import Flask,jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route("/")
def one():
    return "backend is active"

@app.route("/Api")
def apis():
    return jsonify({"msg":"hello from backend"})




app.run(host="0.0.0.0",port=5000)