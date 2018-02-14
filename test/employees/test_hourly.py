import unittest
from employees.Hourly import Hourly


class TestHourly(unittest.TestCase):

    def test_calculate_salary(self):

        hourly_employee = Hourly(1000)
        hourly_employee.add_hours(25)
        result = hourly_employee.calculate_salary()

        expected = 25000

        self.assertEqual(expected, result)

    def test_calculate_salary_without_specifying_hours(self):

        hourly_employee = Hourly(1000)
        result = hourly_employee.calculate_salary()

        expected = 0

        self.assertEqual(expected, result)