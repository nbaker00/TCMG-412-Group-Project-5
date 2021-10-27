from flask import Flask
from flask.scaffold import F
app = Flask(__name__)
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
        







@app.route("/prime")
def isPrime():
    if ans == True:
        return "{}. {} is a Prime Number".format(t,x)
    if ans == False:
        return "{}. {} is not a Prime Number".format(f,x)
