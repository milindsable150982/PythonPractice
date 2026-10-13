class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}, Salary: {self.__salary}")