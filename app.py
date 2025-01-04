from flask import Flask 

app = Flask(__name__)


@app.route("/info")
def main():
    return "Hello new user i am Vivek !!"

app.run(host='0.0.0.0')
