try:
    n=int(input("Enter a number: "))
except Exception as e:
    print(e)
else:
    print(n)