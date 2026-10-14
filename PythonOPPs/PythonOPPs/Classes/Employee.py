class Employee:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")


    def calculate_salary(self):
        return 0  # Base class does not have a salary, so return 0