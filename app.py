from cards.card import Card
from employees import salaried, volunteer, hourly


class App(object):

    def __init__(self, employees=[]):
        self.employees = employees

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_all_workers_salary(self):
        accumulated_salaries = 0
        for employee in self.employees:
            accumulated_salaries += employee.calculate_salary()
        return accumulated_salaries


# APPLICATION functionality goes below

app = App()

salaried_3000 = salaried.Salaried(3000)
salaried_5000 = salaried.Salaried(5000)
volunteer = volunteer.Volunteer()
hourly_150 = hourly.Hourly(150, [])
hourly_150.add_card(Card(10))
hourly_200 = hourly.Hourly(200, [])
hourly_200.add_card(Card(20))

app.add_employee(salaried_3000)
app.add_employee(salaried_5000)
app.add_employee(volunteer)
app.add_employee(hourly_150)  # 1500
app.add_employee(hourly_200)  # 4000

print(app.calculate_all_workers_salary())


