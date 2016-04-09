import unittest
from amity import Amity
from people.Fellow import Fellow


class TestAmity(unittest.TestCase):

    def setUp(self):
        self.amity = Amity()
        self.amity.prepare_amity()

    def tearDown(self):
        self.amity = None

    def test_amity_is_initialised_properly(self):
        self.assertEquals(len(self.amity.offices), 10)
        self.assertEquals(len(self.amity.living), 10)
        self.assertGreater(len(self.amity.people), 0)

    def test_unallocated_fellows_are_returned(self):
        unallocated_fellows = self.amity.get_unallocated_fellows()
        for i in unallocated_fellows:
            self.assertIsInstance(i, Fellow)
            self.assertFalse(i.allocated)

    def test_unallocated_staff_are_returned(self):
        unallocated_staff = self.amity.get_unallocated_staff()
        for i in unallocated_staff:
            self.assertFalse(i.allocated)
