from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    value = request.args.get('value', 'No Value Provided')
    return f'Hello World: {value}'
