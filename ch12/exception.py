#n=int(input("Enter a number: "))
#print(n)
try:
    n = int(input("Enter a number: "))
    print(n)
except ValueError as v:
    print("Heyyy")
    print(v)
except Exception as e:
    print(e)
print("Thank you! ")