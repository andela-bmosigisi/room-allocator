import unittest
from rooms.Office import Office


class TestOffice(unittest.TestCase):

    def setUp(self):
        self.office = Office('Bronx')

    def tearDown(self):
        self.office = None

    def test_office_is_initialized(self):
        self.assertEquals('Bronx', self.office.name)
        self.assertIsInstance(self.office, Office)
        self.assertIsInstance(self.office.allocations, list)

    def test_office_reveals_its_type(self):
        self.assertEquals(self.office.get_type(), 'office')
