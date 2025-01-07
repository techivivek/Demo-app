from flask import Flask 

app = Flask(__name__)


@app.route("/info")
def main():
    return "Hello new user i am Vivek !! and Go To Hell"

app.run(host='0.0.0.0', port=5000)
