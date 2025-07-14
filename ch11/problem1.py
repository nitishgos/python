class Vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show2D(self):
        print(f"Vector2D: ({self.x} , {self.y})")
class Vector3D(Vector2D):
    def __init__(self, x, y,z):
        super().__init__(x, y)
        self.z=z
    def show3D(self):
        print(f"Vector3D: ({self.x} ,{self.y}, {self.z})")
v2=Vector2D(2,3)
v2.show2D()
v3=Vector3D(2,3,4)
v3.show3D()
