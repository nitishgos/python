class Employee:  # Single Inheritance
    company="ITC"
    salary="1200000"
    def getdetails(self):
        print(f"Company name {self.company} and salary is {self.salary}")
class Programmer(Employee):
    company="ITC Infotech"
    language="Python"
    def getstatus(self):
        print(f"Company name {self.company} and language is {self.language}")
employee=Employee()
programmer=Programmer()
print(programmer.salary)
programmer.getdetails()