from  Classes.Employee import *

class PermanentEmployee(Employee):
    def __init__(self, __name, __age, __salary):
        super().__init__(__name, __age)
        self.__salary = __salary

    def calculate_salary(self):
        return self.__salary;

    def display_info(self):
        super().display_info()