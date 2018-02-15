from employees.employee import Employee


class Salaried(Employee):

    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return self.salary
