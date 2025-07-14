class Commplex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __add__(self,other):
        return Commplex(self.real+other.real,self.imag+other.imag)
    def __mul__(self,other):
        real_part=self.real*other.real-self.imag*other.imag
        imag_part=self.real*other.imag+self.imag*other.real
        return Commplex(real_part,imag_part)
    def __str__(self):
        return f"{self.real}+{self.imag}i"
c1=Commplex(2,3)
c2=Commplex(5,6)
c3=c1+c2
c4=c1*c2
print("Sum: ",c3)
print("Product: ",c4)