class Employee:
    def __init__(self,salary,increment):
        self.salary=salary
        self.increment=increment
    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,new_total_salary):
         self.increment = new_total_salary / self.salary
emp = Employee(50000, 1.2)
print("Original salary after increment:", emp.salaryAfterIncrement)
emp.salaryAfterIncrement = 65000
print("New increment:", emp.increment)  
print("Updated salary after increment:", emp.salaryAfterIncrement) 