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

@app.route("/md5")
def main():

        return(hashlib.md5('Hello World'.encode('UTF-8')).hexdigest())
        return "<p>Hello, World!</p>"

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


number = int(input("Enter a number: "))

f = []

a = 0
b = 1
c = 0
if number == 1:
    f.append(a)
elif number < 1:
    print("Please enter a positive integer")
else:
    f.append(a)
    f.append(b)
    while c < number:
        c = a + b
        a = b
        b = c
        f.append(c)

print(f)

@app.route("/fibonacci")
def fib():
    return "The sequence is {}.".format(str(f)[1:-1])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
