a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if(b==0):
    raise ZeroDivisionError("The number cannot divided by zero")
print(f"Division of {a} and {b} is {a/b}")