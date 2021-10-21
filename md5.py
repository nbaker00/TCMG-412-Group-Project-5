from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


#MD5

import hashlib

@app.route("/md5")
def main():

        return(hashlib.md5('Hello World'.encode('UTF-8')).hexdigest())
        return "<p>Hello, World!</p>"
