from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return "<H1> Welcome to Python Backend App </H1> "
    
@app.route('/test', methods=['GET'])
def test_app():
    return "this is a test"
