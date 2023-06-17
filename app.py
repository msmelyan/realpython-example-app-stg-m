# test
# mine
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    value1 = request.args.get('value1', 'No Value Provided')
    value2 = request.args.get('value2', 'No Value Provided')
    return f'Hello World: value1={value1} value2={value2}'
