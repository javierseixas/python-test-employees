import unittest
from employees.hourly import Hourly
from cards.card import Card


class TestHourly(unittest.TestCase):

    def test_calculate_salary(self):

        hourly_employee = Hourly(1000, [])
        hourly_employee.add_card(Card(15))
        hourly_employee.add_card(Card(10))
        result = hourly_employee.calculate_salary()

        expected = 25000

        self.assertEqual(expected, result)

    def test_calculate_salary_without_specifying_hours(self):

        hourly_employee = Hourly(1000, [])
        result = hourly_employee.calculate_salary()

        expected = 0

        self.assertEqual(expected, result)
