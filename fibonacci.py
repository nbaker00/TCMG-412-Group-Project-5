from flask import Flask
app = Flask(__name__)
number = int(input("Enter a number: "))
f =[]

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
