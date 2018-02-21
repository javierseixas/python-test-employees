import unittest
from mock import Mock
from employees.staff import Staff


class TestHourlyCalculator(unittest.TestCase):

    def setUp(self):
        self.staff = Staff([])


    def test_obtain_salary_with_hourly_workers(self):
        hourly_1 = Mock()
        hourly_1.obtain_salary = Mock(return_value=100)
        hourly_2 = Mock()
        hourly_2.obtain_salary = Mock(return_value=400)

        self.staff.add_employee(hourly_1)
        self.staff.add_employee(hourly_2)

        result = self.staff.obtain_salary()
        expected = 500

        self.assertEqual(expected, result)


