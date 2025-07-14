class Employee:
    name="John"
    company="Google"
    @classmethod
    def getdatails(cls):
        print(f"{cls.name} is the employee of {cls.company} company")
employee=Employee()
employee.name="Harry"
employee.company="Microsoft"
employee.getdatails()