n=int(input("Enter the number here"))
i=10
print("The multiplication table in reverse order is: ")
for i in range(10,0,-1):
    print(f"{n}x{i}={n*i}")