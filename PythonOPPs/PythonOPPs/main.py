from Classes.MathOperator import *
from Classes.Employee import *
from Classes.Inheritance.PermanantEmployee import *
from Classes.Inheritance.ContractEmployee import *

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
employee = Employee("milind", 15)
employee.display_info()


print("Inheritance")
contractEmployee = ContractEmployee("priti", 30, 40, 20)
print(f"Contract Employee Info: {contractEmployee.display_info()} and salary is: {contractEmployee.calculate_salary()}")

permanentEmployee = PermanentEmployee("raju", 40, 50000)
print(f"Permanent Employee Info: {permanentEmployee.display_info()} and salary is: {permanentEmployee.calculate_salary()}")


## method overloading

def add(a, b, c=0):
        return a + b + c

print("Addition of 2 numbers:", add(5, 10))
print("Addition of 3 numbers:", add(5, 10, 15))
