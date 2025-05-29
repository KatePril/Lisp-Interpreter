"""
This module provides code for testing executor
"""
import unittest
from unittest.mock import patch
from io import StringIO

from src.executor.executor import execute_node_iterative
from src.parser.parser import tokenize

class MyTestCase(unittest.TestCase):
    """
    This class tests if executor works correctly
    """
    @patch('sys.stdout', new_callable=StringIO)
    def test_one(self, mock_stdout):
        """
        Test case one
        :param mock_stdout:
        :return:
        """
        execute_node_iterative(tokenize("""
            (let ((x 10)
                  (y 20))
                (setf z (+ x y))
                (print z))
            """))
        self.assertEqual(mock_stdout.getvalue().strip(), "30")

    @patch('sys.stdout', new_callable=StringIO)
    def test_two(self, mock_stdout):
        """
        Test case two
        :param mock_stdout:
        :return:
        """
        execute_node_iterative(tokenize("""
                (let ((x 14))
                (if (evenp x)
                  (print x)))
                """))
        self.assertEqual(mock_stdout.getvalue().strip(), "14")

    @patch('sys.stdout', new_callable=StringIO)
    def test_three(self, mock_stdout):
        """
        Test case three
        :param mock_stdout:
        :return:
        """
        execute_node_iterative(tokenize("""
                    (let ((x 15))
                    (if (evenp x)
                      (print x)))
                    """))
        self.assertEqual(mock_stdout.getvalue().strip(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_four(self, mock_stdout):
        """
        Test case four
        :param mock_stdout:
        :return:
        """
        execute_node_iterative(tokenize("""
                (
                    let (
                        (sum 0)
                    )
                    (loop for i from 1 to 10 by 2 do
                        (
                            setf sum (+ sum i)
                        )
                    )
                    (print sum)
                )
                """))
        self.assertEqual(mock_stdout.getvalue().strip(), "25")

if __name__ == '__main__':
    unittest.main()
