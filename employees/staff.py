class Staff(object):

    _employees = []

    def __init__(self, employees):
        self._employees = employees

    def add_employee(self, employee):
        self._employees.append(employee)

    def obtain_salary(self):
        total_salaries = 0
        for employee in self._employees:
            total_salaries += employee.obtain_salary()
        return total_salaries

    def employees(self):
        return self._employees
