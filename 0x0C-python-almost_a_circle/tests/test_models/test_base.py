import unittest
from models.base import Base


class TextBase(unittest.TestCase):

    def test_base_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(15)
        b4 = Base()
        b5 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 15)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, 4)


