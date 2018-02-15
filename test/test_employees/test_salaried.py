import unittest
from employees.salaried import Salaried


class TestSalaried(unittest.TestCase):

    def test_calculate_salary(self):

        salaried_employee = Salaried(10000)
        result = salaried_employee.calculate_salary()

        expected = 10000

        self.assertEqual(expected, result)
