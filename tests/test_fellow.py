import unittest


class TestFellow(unittest.TestCase):

    def setUp(self):
        self.fellow = Fellow('Benjamin Gikera', true)

    def tearDown(self):
        self.fellow = None

    def test_fellow_is_instantiated(self):
        self.assertIsInstance(self.fellow, Fellow, 'Fellow is not created.')

    def test_fellow_details(self):
        self.assertEquals(self.fellow.name, 'Benjamin Gikera')
        self.assertTrue(self.fellow.opt_in)
        self.assertFalse(self.fellow.assigned)
