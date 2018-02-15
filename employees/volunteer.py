from employees.employee import Employee


class Volunteer(Employee):

    SALARY = 0

    def calculate_salary(self):
        return self.SALARY
