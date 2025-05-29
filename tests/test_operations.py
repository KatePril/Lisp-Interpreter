"""
This module provides code for testing operations
"""
import unittest
import sys
from io import StringIO
from src.executor.operations import operators

class TestArithmeticOperations(unittest.TestCase):
    """
    This class tests if operations work correctly
    """
    def test_add_basic(self):
        """
        Test addition with multiple positive integers.
        Expects the sum of 1, 2, and 3 to be 6.
        """
        self.assertEqual(operators.KEYWORDS["+"](1, 2, 3), 6)

    def test_add_empty(self):
        """
        Test addition with no arguments.
        Expects the result to be 0.
        """
        self.assertEqual(operators.KEYWORDS["+"](), 0)

    def test_add_negative(self):
        """
        Test addition with negative and positive integers.
        Expects the sum of -1, -2, and 4 to be 1.
        """
        self.assertEqual(operators.KEYWORDS["+"](-1, -2, 4), 1)

    def test_sub_basic(self):
        """
        Test subtraction with multiple arguments.
        Expects 10 - 2 - 3 to be 5.
        """
        self.assertEqual(operators.KEYWORDS["-"](10, 2, 3), 5)  # 10 - 2 - 3

    def test_sub_single_argument(self):
        """
        Test subtraction with a single argument.
        Expects the result to be the argument itself (7).
        """
        self.assertEqual(operators.KEYWORDS["-"](7), 7)

    def test_sub_empty(self):
        """
        Test subtraction with no arguments.
        Expects the result to be 0.
        """
        self.assertEqual(operators.KEYWORDS["-"](), 0)

    def test_keywords_add(self):
        """
        Test addition using the KEYWORDS mapping.
        Expects 2 + 3 to be 5.
        """
        self.assertEqual(operators.KEYWORDS["+"](2, 3), 5)

    def test_keywords_sub(self):
        """
        Test subtraction using the KEYWORDS mapping.
        Expects 8 - 2 to be 6.
        """
        self.assertEqual(operators.KEYWORDS["-"](8, 2), 6)

    def test_custom_print(self):
        """
        Test the custom print operation.
        Captures output and expects 'hello 123 '.
        """
        captured_output = StringIO()
        sys.stdout = captured_output
        operators.KEYWORDS["print"]("hello", 123)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "\nhello 123 ")
    
    def test_is_equal(self):
        """
        Test equality operation with all equal arguments.
        Expects True for (2, 2, 2, 2).
        """
        self.assertEqual(operators.KEYWORDS["="](2, 2, 2, 2), True)
        
    def test_is_unequal(self):
        """
        Test equality operation with unequal arguments.
        Expects False for (2, 2, 2, 2, 5).
        """
        self.assertEqual(operators.KEYWORDS["="](2, 2, 2, 2, 5), False)

    def test_mul_basic(self):
        """
        Test multiplication with multiple arguments.
        Expects 2 * 3 * 4 to be 24.
        """
        self.assertEqual(operators.KEYWORDS["mul"](2, 3, 4), 24)

    def test_mul_empty(self):
        """
        Test multiplication with no arguments.
        Expects the result to be 1.
        """
        self.assertEqual(operators.KEYWORDS["mul"](), 1)

    def test_div_basic(self):
        """
        Test division with multiple arguments.
        Expects 8 / 2 / 2 to be 2.
        """
        self.assertEqual(operators.KEYWORDS["div"](8, 2, 2), 2)

    def test_div_single(self):
        """
        Test division with a single argument.
        Expects the result to be the argument itself (5).
        """
        self.assertEqual(operators.KEYWORDS["div"](5), 5)

    def test_div_empty(self):
        """
        Test division with no arguments.
        Expects the result to be 0.
        """
        self.assertEqual(operators.KEYWORDS["div"](), 0)

    def test_mod(self):
        """
        Test modulo operation.
        Expects 10 % 3 to be 1.
        """
        self.assertEqual(operators.KEYWORDS["mod"](10, 3), 1)

    def test_is_more(self):
        """
        Test greater-than comparison.
        Expects True for (5, 2) and False for (2, 5).
        """
        self.assertTrue(operators.KEYWORDS[">"](5, 2))
        self.assertFalse(operators.KEYWORDS[">"](2, 5))

    def test_is_less(self):
        """
        Test less-than comparison.
        Expects True for (2, 5) and False for (5, 2).
        """
        self.assertTrue(operators.KEYWORDS["<"](2, 5))
        self.assertFalse(operators.KEYWORDS["<"](5, 2))

    def test_and(self):
        """
        Test logical AND operation.
        Expects True for (True, True) and False for (True, False).
        """
        self.assertTrue(operators.KEYWORDS["and"](True, True))
        self.assertFalse(operators.KEYWORDS["and"](True, False))

    def test_or(self):
        """
        Test logical OR operation.
        Expects True for (True, False) and False for (False, False).
        """
        self.assertTrue(operators.KEYWORDS["or"](True, False))
        self.assertFalse(operators.KEYWORDS["or"](False, False))

    def test_not(self):
        """
        Test logical NOT operation.
        Expects True for (False) and False for (True).
        """
        self.assertTrue(operators.KEYWORDS["not"](False))
        self.assertFalse(operators.KEYWORDS["not"](True))

    def test_let(self):
        """
        Test the let operation for variable binding.
        Expects a dictionary with variable names and values.
        """
        class DummyNode:
            """
            TestClass
            """
            def __init__(self, tokens):
                self.tokens = tokens
        nodes = [DummyNode(["x", 42]), DummyNode(["y", 99])]
        result = operators.KEYWORDS["let"](nodes)
        self.assertEqual(result, {"x": 42, "y": 99})

if __name__ == '__main__':
    unittest.main()
