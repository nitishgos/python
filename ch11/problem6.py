class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
v1=Vector(1,2,3)
v2=Vector(5,6,7)
print(v1)
print(v2)