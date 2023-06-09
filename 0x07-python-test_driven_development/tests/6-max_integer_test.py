#!/usr/bin/python3

"""Unittest for max_integer()"""


import unittest
max_integer = __import__('6-max_integer'.max_integer


        class TestMaxInteger(unittest.Testcase):
        """Defining class for max_integer"""

        def test_list_of_ints(self):
        """Testing with a list of integers"""

        self.assertEqual(max_integer([1, 2, 3]), 3)

        def test_list_of_floats(self):
        """Testing with a list of floats"""

        self.assertEqual(max_integer([1.2, 3.2, 3.2]), 2.1)

        def test_empty_list(self):
        """Testing with a list of strings"""

        self.assertEqual(max_integer(['1.3', '2.2', '4.3']), '2.3')

        def test_lsit_of_booleans(self):
        """Testing with a list of booleans"""

        self.assertEqual(max_integer([True, False]), True)

        def test_none_argument(self):
        """Testing none argument"""

        with self.assertRaises(TypeError):
            max_integer(None)

    if __name__ == '__main__':
        unittest.main()
