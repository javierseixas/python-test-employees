import unittest

from cards.card import Card
from employees.volunteer import Volunteer
from employees.hourly import Hourly
from employees.salaried import Salaried
from app import App


class TestApp(unittest.TestCase):

    def test_app_calculates_correctly_all_employees_total_salaries(self):

        volunteer = Volunteer()
        salaried = Salaried(1000)
        hourly = Hourly(100, [Card(10)])
        test_employees = [volunteer, salaried, hourly]

        application = App(test_employees)
        result = application.calculate_all_workers_salary()
        expected = 2000

        self.assertEqual(expected, result)
