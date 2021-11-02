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

x= int(input("Enter a number: "))
ans=0
if x > 1:
    for i in range(2, x):
        if x % i == 0:

            f = (False)
            ans=False
            print(ans)
            break
    else:

        t= (True)
        ans = True
        print(ans)

@app.route("/is-prime")
def isPrime():
    if ans == True:
        return "{}. {} is a Prime Number".format(t,x)
    if ans == False:
        return "{}. {} is not a Prime Number".format(f,x)



import math

n = int(input("Enter a number: "))
fact = 1

for i in range(1,n+1):
   fact = fact * i

if n >= 0:
   print("The factorial of the number is: ",end="")
   print(fact)
else:
   print("Please enter a non negative integer")
@app.route("/factorial")
def factorial():
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
