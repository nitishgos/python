class Employee:  # Single Inheritance
    company="ITC"
    salary="1200000"
    def getdetails(self):
        print(f"Company name {self.company} and salary is {self.salary}")
class Programmer():
    company="ITC Infotech"
    language="Python"
    def getstatus(self):
        print(f"Company name {self.company} and language is {self.language}")
class Manager(Employee,Programmer):
    role="Manager"
    def getrole(self):
        print(f"Role is {self.Role}")
manager=Manager()
manager.getdetails()
manager.getstatus()
print(manager.role)
