number = int(input("Enter a number: "))

def fib(number):
    a = 0
    b = 1
    c = 0
    if number == 1:
        print(a)
    elif number < 1:
        print("Please enter a positive integer")
    else:
        print(a)
        print(b)
        while c < number:
            c = a + b
            a = b
            b = c
            print(c)

fib(number)
  