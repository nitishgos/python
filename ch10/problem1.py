class Programmer:
    company="Microsoft"
    def __init__(self,name,age,gender,position,salary):
        self.name=name
        self.age=age
        self.gender=gender
        self.position=position
        self.salary=salary
    def getdetails(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Position:",self.position)
        print("Salary:",self.salary)
p1=Programmer("Nitish",21,"Male","Microsoft",170000)
p1.getdetails()
p2=Programmer("Alice", 28, "Male","Microsoft",200000)
p2.getdetails()

