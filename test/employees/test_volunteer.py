import unittest
from employees.Volunteer import Volunteer


class TestSalaried(unittest.TestCase):

    def test_calculate_salary(self):

        volunteer_employee = Volunteer()
        result = volunteer_employee.calculate_salary()

        expected = 0

        self.assertEqual(expected, result)
