from employees.employee import Employee


class Hourly(Employee):

    def __init__(self, salary_per_hour, worked_hours=0):
        self.worked_hours = worked_hours
        self.salary_per_hour = salary_per_hour

    def add_hours(self, hours):
        self.worked_hours += hours

    def calculate_salary(self):
        return self.salary_per_hour * self.worked_hours
