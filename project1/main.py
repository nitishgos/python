'''
1 for snake
-1 for water
0 for gun
'''
import random
computer=random.choice([-1,0,1])
youstr=input("Enter your choice form (s,w,g): ")
youDict={"s":1,"w":-1,"g":0}
dictReverse={1:"s",-1:"w",0:"g"}
if youstr not in youDict:
    print("Invalid input! Please enter 's' for Snake, 'w' for Water, or 'g' for Gun.")
else:
    you = youDict[youstr]
    print(f"You chose {dictReverse[you]}. Computer chose {dictReverse[computer]}.")
if(you == computer):
    print("It's a tie")
elif((you == 1 and computer==-1) or (you==-1 and computer==0) or (you==0 and computer==1)):
    print("You Win!")
else:
    print("You loose!")