p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"
message=input("Enter a message here: ")
if((p1 in message)or(p2 in message)or(p3 in message)):
    print("The message is spam")
else:
    print("The message is not spam")