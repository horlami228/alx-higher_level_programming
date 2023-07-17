import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_rectangle_id(self):
        r1 = Rectangle(11, 4)
        r2 = Rectangle(4, 7)
        r3 = Rectangle(10, 5, 1, 1, 67)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 67)

    def test_validate_attributes(self):
        with self.assertRaises(TypeError):
            Rectangle(width="lekan", height=5, x=1, y=1)
        with self.assertRaises(TypeError):
            Rectangle(width=9, height="lekan", x=1, y=1)
        with self.assertRaises(ValueError):
            Rectangle(width=-1, height=10, x=1, y=1)
        with self.assertRaises(ValueError):
            Rectangle(width=11, height=-1, x=1, y=1)
        with self.assertRaises(ValueError):
            Rectangle(width=11, height=10, x=-1, y=1)
        with self.assertRaises(TypeError):
            Rectangle(width=11, height=10, x="x", y=1)
        with self.assertRaises(TypeError):
            Rectangle(width=11, height=10, x=1, y="y")
        with self.assertRaises(ValueError):
            Rectangle(width=11, height=10, x=1, y=-1)

    def test_area(self):
        rec = Rectangle(10, 5)
        rec1 = Rectangle(2, 8)

        self.assertEqual(50, rec.area())
        self.assertEqual(16, rec1.area())

    def test_print_display(self):
        rectangle = (4, 5)

        self.assertEqual("####"
                         "####"
                         "####"
                         "####"
                         "", rectangle.display())
