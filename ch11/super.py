class Employee:
    def __init__(self):
        print("Constructor for Employee")
    a=10
class Programmer(Employee):
    def __init__(self):
        #super().__init__()
        print("Constructor for Programmer")
    b=20
class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor for Manager")
    c=30
# programmer=Programmer()
# print(programmer.b)
manager=Manager()
print(manager.c)
