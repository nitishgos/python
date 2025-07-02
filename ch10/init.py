class Employee:  # class name
    name="Rohan"  # This is class Attribute
    language="py"
    salary=1200000
    def __init__(self,name,language,salary):
        self.name=name
        self.language=language
        self.salary=salary
    def getsalary(self):
        print(f"name: {self.name} language: {self.language} salary: {self.salary}")
nitish=Employee("Nitish","Java",1400000) # object creation
print(nitish.name,nitish.language,nitish.salary)
nitish.getsalary()