class Employee:  # class name
    name="Rohan"  # This is class Attribute
    language="py"
    salary=1200000
    def getsalary(self):
        print(f"name: {self.name} language: {self.language} salary: {self.salary}")
    @staticmethod
    def greet():
        print("Good morning")
nitish=Employee() # object creation
# nitish.name="Nitish" # This is object attribute (object attribute)
nitish.greet()
# print(nitish.name,nitish.language,nitish.salary)
nitish.getsalary() # Also we can write Employee.getsalary(nitish)