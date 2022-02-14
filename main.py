from email import message
from sre_constants import SUCCESS
from flask import Flask,jsonify, request
from data import data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return jsonify({
        "data" : data,
        "message":"Success"
    }),200

@app.route("/name")
def star():
    name=request.args.get("name")
    star_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data" : star_data,
        "message" : "Success" 
    }),200

if (__name__ == "__main__"):
    app.run(debug=True)