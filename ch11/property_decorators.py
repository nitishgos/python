class Employee:
    def __init__(self):
        print("Constructor for Employee")
    a=10
    @property
    def name(self):
        return self.ename
    @name.setter
    def name(self,value):
        self.ename=value
employee=Employee()
employee.name="Nitish"
print(employee.name)
