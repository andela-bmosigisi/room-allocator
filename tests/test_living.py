import unittest
from mock import MagicMock
from rooms.Living import Living


class Test(unittest.TestCase):

    def setUp(self):
        self.living = Living('Bronx')

    def tearDown(self):
        self.living = None

    def test_allocations_are_returned(self):
        allocations = self.living.get_allocations()
        self.assertIsInstance(allocations, list)

    def test_rooms_are_allocated(self):
        # pass a mocked person object.
        person = MagicMock(name='person')
        person.get_type = MagicMock(return_value='fellow')
        person.opt_in = True
        self.assertTrue(self.living.allocate_room(person))
        self.assertEquals(len(self.living.allocations), 1)
        self.assertEquals(self.living.allocations[0], person)

    def test_wrong_people_are_not_allocated(self):
        person = MagicMock(name='person')
        # staff shouldn't be allocated rooms.
        person.get_type = MagicMock(return_value='staff')
        self.assertFalse(self.living.allocate_room(person))
        self.assertEquals(len(self.living.allocations), 0)
        # fellows who choose not to live shouldn't be allocated.
        person.get_type = MagicMock(return_value='fellow')
        person.opt_in = False
        self.assertFalse(self.living.allocate_room(person))
        self.assertEquals(len(self.living.allocations), 0)

    def test_get_type(self):
        self.assertEqual('living', self.living.get_type())


if __name__ == '__main__':
    unittest.main()
