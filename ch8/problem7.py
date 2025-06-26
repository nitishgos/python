def remove(l,word):
    n=[]
    for i in l:
        if not(i==word):
            n.append(i.strip(word))
        
    return n



l=['Nitish','Rohan','Rajveer','Ankan']
print(remove(l,"an"))