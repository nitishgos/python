sub1=float(input("Enter the first subject marks: "))
sub2=float(input("Enter the second subject marks: "))
sub3=float(input("Enter the third subject marks: "))
total=sub1+sub2+sub3
percentage=(total/300)*100
if(sub1>=33 and sub2>=33 and sub3>=33) and (percentage>=40):
    print("Congratulations! You passed the exam")
else:
    print("Sorry! you failed the exam")
print("The total is: ",total)