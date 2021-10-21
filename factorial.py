# Python code to demonstrate naive method
# to compute factorial
n = int(input("Enter a number: "))
fact = 1


for i in range(1,n+1):
    fact = fact * i
    
if n >= 0:
    print ("The factorial of the number is: ",end="")
    print(fact)
else:
    print("Please enter a non negative integer")