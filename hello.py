from flask import Flask
from flask import jsonify

#import os
#import socket

#redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

import hashlib
    
@app.route("/md5/<string:word>")
def main(word):

        hash = hashlib.md5(word.encode())
        return jsonify(input=word, output=hash.hexdigest())

@app.route("/is-prime/<int:x>")   
def isPrime(x):    
    ans=0
    if x > 1:
        for i in range(2, x):
            if x % i == 0:

                f = (False)
                ans= False
                break
        else:

            t= (True)
            ans = True  
    if ans == True:
        return jsonify(input=x, output=True)
    if ans == False:
        return jsonify(input=x, output=False)



import math

@app.route("/factorial/<int:n>")
def factorial(n):

    fact = 1

    for i in range(1,n+1):
        fact = fact * i



    return jsonify({'input':n, "output": fact})

@app.route("/fibonacci/<int:number>")
def fib(number):
    f = []

    a = 0
    b = 1
    c = 0
    if number == 1:
        f.append(a)

    else:
        f.append(a)
        f.append(b)
        while c < number:
            c = a + b
            a = b
            b = c
            f.append(c)
    return jsonify(input=number, output=f)



import requests
import sys
import getopt

#send message to slack
import requests
import sys
import getopt

#send message to slack

def send_slack_message(message):
    payload = '{"text": "%s"}' % message
    response = requests.post('https://hooks.slack.com/services/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',
                            data=payload)
    print(response.text)


def main(argv):

    message = ' '

    try: opts, args = getopt.getopt(argv, "hm:", ["message"])

    except getopt.GetoptError:
        print("SlackMessage.py -m <message>")
        sys.exit(2)
    if len(opts) == 0:
        message = "Hello. It works!"
    for opt, arg in opts:
        if opt == '-h':
            print("SlackMessage.py -m <message>")
            sys.exit()
        elif opt in ("-m", "--message"):
            message = arg

    send_slack_message(message)


if __name__ == "__hello__":
    main(sys.argv[1:])

    
    
# Get CRUD

@app.route("/keyval/<collection>")
def get_collection(collection):


    if collection in stock:
        res = make_response(jsonify(stock[collection]), 200)
        return res

    res = res = make_response(jsonify({"error": "Not found"}), 404)

    return res



