import unittest
from people.Staff import Staff


class TestStaff(unittest.TestCase):

    def setUp(self):
        self.staff = Staff('Martin Luther')

    def tearDown(self):
        self.staff = None

    def test_staff_is_instantiated(self):
        self.assertIsInstance(self.staff, Staff, 'Staff is not created.')

    def test_staff_properties(self):
        self.assertEquals(self.staff.name, 'Martin Luther')

if __name__ == '__main__':
    unittest.main()
