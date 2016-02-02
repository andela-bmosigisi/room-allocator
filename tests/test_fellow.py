import unittest
from people.Fellow import Fellow


class TestFellow(unittest.TestCase):

    def setUp(self):
        self.fellow = Fellow('Benjamin Gikera', True)

    def tearDown(self):
        self.fellow = None

    def test_fellow_is_instantiated(self):
        self.assertIsInstance(self.fellow, Fellow, 'Fellow is not created.')
        self.assertEqual(self.fellow.get_type(), 'fellow')

    def test_fellow_details(self):
        self.assertEquals(self.fellow.name, 'Benjamin Gikera')
        self.assertTrue(self.fellow.opt_in)
        self.assertFalse(self.fellow.allocated)

if __name__ == '__main__':
    unittest.main()
