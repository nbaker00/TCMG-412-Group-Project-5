from flask import Flask, jsonify, request
import redis
from redis import Redis, StrictRedis, RedisError

import os
#import socket

redis = redis.StrictRedis('redis-server', 6379, charset="utf-8", decode_responses=True)

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



#send message to slack
@app.route("/slack-alert/<string:message>")
def sendslackmessage(message):
    #create the slack client
    import slack_sdk 
    from slack_sdk.errors import SlackApiError   
    try:
        client = slack_sdk.WebClient(token=os.environ['SLACK_TOKEN'])
    except:
        return jsonify(input=message, output=False, error='Could not talk to slack service'), 503
    
    #send slack the message
    try:
        response = client.chat_postMessage(channel="C011KJWHA22", text=message)
    except SlackApiError as e:
        return jsonify(input=message, output=False, error='there was a slack api error'), 500
        
    #check for success
    if response.status_code == 200:
        return jsonify(input=message, output=True)
    else:
        return jsonify(input=message, output=False, error='slack returns not 200 error'), 502

    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)



@app.route("/keyval/<collection>")
def get_collection(collection):


    if collection in stock:
        res = make_response(jsonify(stock[collection]), 200)
        return res

    res = res = make_response(jsonify({"error": "Not found"}), 404)

    return res

@app.route('/keyval/<string>'), methods=['DELETE']
def handle_delete():
    if keys in database:
       del database[keys]
       res = make_response(jsonify({}), 204)
       return res

@app.route('/keyval', methods=['PUT'])
def handle_put():
    client_data = request.get_json()
    if client_data.get('marc'):
        k = client_data.get('marc')

    
@app.route('/keyval', methods=['POST'])
def handle_post():
    client_data = request.get_json()
    if client_data.get('marc'):
        k = client_data.get('marc')
    else:
        k = ''

        err_string = "Invalid JSON from client: No key found"
        return jsonify(
            key=k,
            value=v,
            command=f"CREATE {k}/{v}",
            result=False,
            error=err_string
        ), 400

    v = client_data['21']

    if redis.exists(k):
        return jsonify(), 409
    redis_result = redis.set(k,v)
    if redis_result == False:
        err_string = "There was a problem writing to the db"
    else:
        err_string = None

    return jsonify(
        key=k,
        value=v,
        command=f"CREATE {k}/{v}",
        result=redis_result,
        error=err_string
    ), 400
