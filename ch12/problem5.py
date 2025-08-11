num=int(input("Enter a number: "))
multable=[num*i for i in range(1,11)]
print(multable)
with open("Tables.txt","w") as f:
    f.write(f"Multiplication table of {num}:\n")
    for i,val in enumerate(multable):
        f.write(f"{num} x {i+1} = {val}\n")
print("Table saved to Tables.txt successfully")