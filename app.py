from accountant import Accountant
from employees import Staff
from employees import Employee
from contracts import *
from salary_calculators import *
from cards.card import Card

class App(object):

    def __init__(self):
        self._accountant = Accountant()

    def execute(self):
        staff = self._create_staff_fixtures()
        print(self._accountant.calculate_staff_salary(staff))

    def _create_staff_fixtures(self):
        return Staff([self._new_employee(10, 'hourly', [10, 5])])


    def _new_employee(self, salary, contract, tracked_hours):
        if contract == 'hourly':
            cards = []
            for hours in tracked_hours:
                cards.append(Card(hours))
            return Employee(Hourly(salary), HourlyCalculator(), cards)

        if contract == 'voluntary':
            cards = []
            for hours in tracked_hours:
                cards.append(Card(hours))
            return Employee(Voluntary(), HourlyCalculator(), cards)

        if contract == 'fixed':
            cards = []
            for hours in tracked_hours:
                cards.append(Card(hours))
            return Employee(Fixed(salary), HourlyCalculator(), cards)

        pass

app = App()
app.execute()