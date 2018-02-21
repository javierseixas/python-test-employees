import unittest
from mock import Mock
from employees import Staff


class TestHourlyCalculator(unittest.TestCase):

    def setUp(self):
        self.staff = Staff([])


    def test_obtain_salary_with_hourly_employees(self):
        hourly_1 = Mock()
        hourly_1.obtain_salary = Mock(return_value=100)
        hourly_2 = Mock()
        hourly_2.obtain_salary = Mock(return_value=400)

        self.staff.add_employee(hourly_1)
        self.staff.add_employee(hourly_2)

        result = self.staff.obtain_salary()
        expected = 500

        self.assertEqual(expected, result)


    def test_obtain_salary_with_fixed_employees(self):

        fixed_1 = Mock()
        fixed_1.obtain_salary = Mock(return_value=1000)
        fixed_2 = Mock()
        fixed_2.obtain_salary = Mock(return_value=3000)

        self.staff.add_employee(fixed_1)
        self.staff.add_employee(fixed_2)

        result = self.staff.obtain_salary()
        expected = 4000

        self.assertEqual(expected, result)


    def test_obtain_salary_for_mixed_kind_of_employees(self):
        hourly = Mock()
        hourly.obtain_salary = Mock(return_value=100)

        fixed = Mock()
        fixed.obtain_salary = Mock(return_value=1000)

        volunteer = Mock()
        volunteer.obtain_salary = Mock(return_value=0)

        self.staff.add_employee(hourly)
        self.staff.add_employee(fixed)
        self.staff.add_employee(volunteer)

        result = self.staff.obtain_salary()
        expected = 1100

        self.assertEqual(expected, result)