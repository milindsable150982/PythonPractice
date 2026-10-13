from Classes.MathOperator import *
from Classes.Employee import *

## Functions
def myFunction(firstName, lastName):
    print(f"This is {firstName} {lastName}'s first function in Python")

myFunction("milind", "Sable")

def myFunction2(firstname, lastname, age):
    return {
        "firstName": firstname,
        "lastName": lastname,
        "age": age
    }

print(myFunction2("milind", "sable", 25))

## Constructor and functions
simpleMath = MathOperator()
print("Addition:", simpleMath.Add())
print("Subtraction:", simpleMath.Subtract())
print("Multiplication:", simpleMath.multiply())
print("Division:",  simpleMath.divide())   


## Parameterized Constructor
employee = Employee("milind", 25, 50000)
employee.display_info()