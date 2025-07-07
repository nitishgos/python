class Calculator:
    def __init__(self,num):
        self.num = num
    def square(self):
        return self.num ** 2
    def cube(self):
        return self.num ** 3
    def square_root(self):
        return self.num ** 0.5
    @staticmethod
    def greet():
        print("Hello there")
num1=Calculator(25)
num1.greet()
print(num1.square()) # Output: 625
print(num1.cube()) # Output: 15625
print(num1.square_root()) # Output: 5

num2=Calculator(36)
num2.greet()
print(num2.square()) # Output: 1296
print(num2.cube())
print(num2.square_root())