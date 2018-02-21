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
        return Staff([
            self._new_employee(150, 'hourly', [5, 5]),
            self._new_employee(200, 'hourly', [10, 5, 5]),
            self._new_employee(3000, 'fixed', [40, 40, 40, 38]),
            self._new_employee(5000, 'fixed', [40, 40, 40, 43]),
            self._new_employee(0, 'voluntary', [50, 50, 60, 50]),
        ])


    def _new_employee(self, salary, contract, tracked_hours):
        if contract == 'hourly':
            cards = self._from_hours_to_cards(tracked_hours)
            return Employee(Hourly(salary), HourlyCalculator(), cards)

        if contract == 'voluntary':
            cards = self._from_hours_to_cards(tracked_hours)
            return Employee(Voluntary(), VoluntaryCalculator(), cards)

        if contract == 'fixed':
            cards = self._from_hours_to_cards(tracked_hours)
            return Employee(Fixed(salary), FixedCalculator(), cards)

        pass

    def _from_hours_to_cards(self, tracked_hours):
        cards = []
        for hours in tracked_hours:
            cards.append(Card(hours))
        return cards


app = App()
app.execute()