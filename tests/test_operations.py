import unittest
from executor.operations import operators
from io import StringIO
import sys

class TestArithmeticOperations(unittest.TestCase):

    def test_add_basic(self):
        self.assertEqual(operators.KEYWORDS["+"](1, 2, 3), 6)

    def test_add_empty(self):
        self.assertEqual(operators.KEYWORDS["+"](), 0)

    def test_add_negative(self):
        self.assertEqual(operators.KEYWORDS["+"](-1, -2, 4), 1)

    def test_sub_basic(self):
        self.assertEqual(operators.KEYWORDS["-"](10, 2, 3), 5)  # 10 - 2 - 3

    def test_sub_single_argument(self):
        self.assertEqual(operators.KEYWORDS["-"](7), 7)

    def test_sub_empty(self):
        self.assertEqual(operators.KEYWORDS["-"](), 0)

    def test_keywords_add(self):
        self.assertEqual(operators.KEYWORDS["+"](2, 3), 5)

    def test_keywords_sub(self):
        self.assertEqual(operators.KEYWORDS["-"](8, 2), 6)

    def test_custom_print(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        operators.KEYWORDS["print"]("hello", 123)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "hello 123 ")
    
    def test_is_equal(self):
        self.assertEqual(operators.KEYWORDS["=="](2, 2, 2, 2), True)
        
    def test_is_unequal(self):
        self.assertEqual(operators.KEYWORDS["=="](2, 2, 2, 2, 5), False)


if __name__ == '__main__':
    unittest.main()
