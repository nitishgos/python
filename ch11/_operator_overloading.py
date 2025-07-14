class Number:
    def __init__(self,n):
        self.n=n
    
    def __add__(self,num):
        return self.n+num.n
    def __sub__(self,num):
        return self.n-num.n
p=Number(2)
q=Number(3)
print(p+q)
print(p-q)