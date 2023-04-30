"""
usefulib v1.0.4
Copyright Hamd Waseem (https://github.com/hamdivazim) under the GNU Public License 3.0.

https://github.com/hamdivazim/usefulib


This is where you should write unit tests for your useful method. If you can't do so for any reason, mention so in your PR so I can help.
"""

import unittest
from _usefulibs import *

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

    def test_external_verbose_output(self):
        """ @hamdivazim """
        external_verbose_output("Test Data\n1 2 3\na b c", R"usefulib\temp_data\ext_verbose_test.log")

        with open(R"usefulib\temp_data\ext_verbose_test.log", "r") as f:
            self.assertEqual(f.read(), "# Logged by usefulibs.external_verbose_output()\n\nTest Data\n1 2 3\na b c")

    def test_get_hash(self):
        """ @MKM12345 + @hamdivazim """
        self.assertEqual(get_hash("abc123"), get_hash("abc123"))
        self.assertRaises(TypeError, get_hash, 1)
        
    def test_denary_to_ternary(self):
        """ @AtomicCodeLegend """
        self.assertEqual(denary_to_ternary(20), 202)
        self.assertEqual(denary_to_ternary(86), 10012)
        self.assertEqual(denary_to_ternary(1), 1)
         def test_convert_base(self):
        # test case 1
        user_input = ['10', '2', '13']
        expected_output = "The number in base 2 is: 1101"
        with unittest.mock.patch('builtins.input', side_effect=user_input), \
             unittest.mock.patch('builtins.print') as mock_print:
            convert_base()
            mock_print.assert_called_with(expected_output)

        # test case 2
        user_input = ['2', '16', '1101']
        expected_output = "The number in base 16 is: D"
        with unittest.mock.patch('builtins.input', side_effect=user_input), \
             unittest.mock.patch('builtins.print') as mock_print:
            convert_base()
            mock_print.assert_called_with(expected_output)

if __name__ == "__main__":
    unittest.main()
