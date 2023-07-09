#!/usr/bin/python3
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([])"""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4, 5, 6]
        expected_result = 6

        actual_result = max_integer(ordered)
        self.assertEqual(expected_result, actual_result)

    def test_unordered_list(self):
        """Test with an unordered list"""
        unordered = [1, 4, 2, 8, 5]

        expected_result = 8
        actual_result = max_integer(unordered)

        self.assertEqual(expected_result, actual_result)

    def test_max_at_end(self):
        """Test with the max number at the end"""
        test_list = [1, 10, 2, 55]

        expected_result = 55
        actual_result = max_integer(test_list)

        self.assertEqual(expected_result, actual_result)

    def test_max_at_beginning(self):
        """Test with max at the beginning"""
        test_list = [70, 20, 0, 17, 48]

        expected_result = 70
        actual_result = max_integer(test_list)

        self.assertEqual(expected_result, actual_result)

    def test_max_at_middle(self):
        """Test with max in the middle"""
        test_list = [1, 2, 4, 7, 3, 3, 0]

        expected_result = 7
        actual_result = max_integer(test_list)

        self.assertEqual(expected_result, actual_result)

    def test_one_negative_number(self):
        """Test with max in the middle"""
        test_list = [1, 2, 4, 7, 3, -3, 0]

        expected_result = 7
        actual_result = max_integer(test_list)

        self.assertEqual(expected_result, actual_result)

    def test_max_at_all_negative_numbers(self):
        """Test with max in the middle"""
        test_list = [-1, -2, -4, -7, -3, -3]

        expected_result = -1
        actual_result = max_integer(test_list)

        self.assertEqual(expected_result, actual_result)

    def test_list_one_element(self):
        """Test with max in the middle"""
        test_list = [10]

        expected_result = 10
        actual_result = max_integer(test_list)

        self.assertEqual(expected_result, actual_result)

    def test_empty_list(self):
        """Test with max in the middle"""
        test_list = []

        expected_result = None
        actual_result = max_integer(test_list)

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
