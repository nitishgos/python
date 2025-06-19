num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
num4=int(input("Enter the fourth number: "))
greatest=num1
if(num2>greatest):
    greatest=num2
if(num3>greatest):
    greatest=num3
if(num4>greatest):
    greatest=num4
print("Greatest number among this four number is: ",greatest)