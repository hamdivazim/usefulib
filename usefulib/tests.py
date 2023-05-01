"""
usefulib v1.0.5
Copyright Hamd Waseem (https://github.com/hamdivazim) under the GNU Public License 3.0.

https://github.com/hamdivazim/usefulib


This is where you should write unit tests for your useful method. If you can't do so for any reason, mention so in your PR so I can help.
"""

import unittest
from _usefulibs import *

def write_to_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)

def read_from_file(filename):
    with open(filename, "r") as f:
        return f.read()

class TestUsefulibs(unittest.TestCase):

    def setUp(self):
        # For now, there are no setup scripts for tests. If you need to add one, remove this comment and add it.
        pass

    def test_reverse_string(self):
        """ @hamdivazim """

        self.assertEqual(reverse_string("abc"), "cba")
        self.assertEqual(reverse_string("123abcdef456"), "654fedcba321")

    def test_loop_dict(self):
        """ @hamdivazim """
        test_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

        self.assertEqual(loop_dict(test_dict), [("a", 1, 0),("b", 2, 1),("c", 3, 2),("d", 4, 3),("e", 5, 4),])

        index = 0
        for key, val, i in loop_dict(test_dict):
            if index == 1:
                self.assertEqual(key, "b")
                self.assertEqual(val, 2)
                self.assertEqual(i, 1)
            
            index += 1

    def test_find_nth_root(self):
        """ @hamdivazim """
        self.assertEqual(find_nth_root(8, 3), 2)
        self.assertEqual(find_nth_root(729, 6), 3)
        self.assertEqual(find_nth_root(4, -2), 0.5)
        self.assertRaises(ValueError, find_nth_root, -4, -2)

    def test_filter_by_string(self):
        """ @hamdivazim """
        lst = ["I really do love apples!", "Bananas are nice!", "An apple a day keeps the doctor away!", "You want a pear?"]
        lst2 = [1, "I really do love apples!", "Bananas are nice!", "An apple a day keeps the doctor away!", "You want a pear?"]

        self.assertEqual(filter_by_string(lst, "apple")[1], "An apple a day keeps the doctor away!")
        self.assertRaises(TypeError, filter_by_string, lst2, "apple")

    def test_filter_by_condition(self):
        """ @hamdivazim """
        self.assertEqual(filter_by_condition([0,1,2,3,4,5,6,7,8,9,10], "i % 2 == 0"), [0, 2, 4, 6, 8, 10])
        self.assertEqual(filter_by_condition(["123abc", "456def", "123456"], '"123" in i'), ["123abc", "123456"])

    def test_generate_random_string(self):
        """ @hamdivazim """
        self.assertNotEqual(generate_random_string(18), generate_random_string(18))

    def test_generateUUID(self):
        """ @hamdivazim """
        self.assertNotEqual(generateUUID(), generateUUID())
        self.assertRaises(ValueError, generateUUID, 6)

    def test_get_hash(self):
        """ @MKM12345 + @hamdivazim """
        self.assertEqual(get_hash("abc123"), get_hash("abc123"))
        self.assertRaises(TypeError, get_hash, 1)
        
    def test_denary_to_ternary(self):
        """ @AtomicCodeLegend """
        self.assertEqual(denary_to_ternary(20), 202)
        self.assertEqual(denary_to_ternary(86), 10012)
        self.assertEqual(denary_to_ternary(1), 1)

    def test_is_palindrome(self):
        """ @TheCodingLedendofTheNether + MKM12345 """
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello world"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_calculate_fibonacci(self):
        """ @TheCodingLedendofTheNether + MKM12345"""
        self.assertEqual(calculate_fibonacci(0), 0)
        self.assertEqual(calculate_fibonacci(1), 1)
        self.assertEqual(calculate_fibonacci(2), 1)
        self.assertEqual(calculate_fibonacci(3), 2)
        self.assertEqual(calculate_fibonacci(4), 3)
        self.assertEqual(calculate_fibonacci(5), 5)
        self.assertEqual(calculate_fibonacci(6), 8)
        
    def test_convert_base(self):
        self.assertEqual(convert_base(2, 10, '1010'), '10')
        self.assertEqual(convert_base(10, 2, '10'), '1010')
        self.assertEqual(convert_base(16, 8, '3E8'), '1750')
        self.assertEqual(convert_base(8, 16, '1750'), '3E8')
        self.assertEqual(convert_base(2, 16, '101010'), '2A')
        self.assertEqual(convert_base(16, 2, '2A'), '101010')
        self.assertEqual(convert_base(10, 16, '255'), 'FF')
        self.assertEqual(convert_base(16, 10, 'FF'), '255')

if __name__ == "__main__":
    unittest.main()
