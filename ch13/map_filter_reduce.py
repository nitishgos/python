from functools import reduce
# map function
l=[1,2,3,4,5]
square=lambda x:x*x
sqlist=map(square,l)
print(list(sqlist))
 
 #Filter function
def even(n):
    if(n%2==0):
        return True
    return False
onlyeven=filter(even,l)
print(list(onlyeven))
# Reduce function
def add(a,b):
    return a+b
def mul(a,b):
    return a*b
val=reduce(add,l)
print(val)
val2=reduce(mul,l)
print(val2)
