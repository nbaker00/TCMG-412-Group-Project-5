#added the route for Prime
@app.route("/prime")

def isPrime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False

        return True

    return False

print(isPrime(int(input("Enter a number: "))))
