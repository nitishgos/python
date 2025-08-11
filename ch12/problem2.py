mylist=[10,20,30,40,50,60,70,80,90,100]
for index,item in enumerate(mylist):
    if index in(3,5,7):
        print(f"{index}th element: {item}")