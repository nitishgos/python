n=int(input("Enter a number here: "))
c=0
for i in range(2,n):
    if n%i==0:
        c=c+1
if c==1:
    print(f"The number {n} is prime")
else:
    print(f"The number {n} is not prime")