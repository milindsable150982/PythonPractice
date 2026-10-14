from  Classes.Employee import *

class ContractEmployee(Employee):

    def __init__(self, __name, __age, __hours_worked, __hourly_rate):
        super().__init__(__name, __age)  # Call parent constructor with default salary
        self.__hours_worked = __hours_worked
        self.__hourly_rate = __hourly_rate

    def calculate_salary(self):
        return self.__hourly_rate * self.__hours_worked * 20 #20 is the number of working days in a month

    def display_info(self):
        super().display_info()