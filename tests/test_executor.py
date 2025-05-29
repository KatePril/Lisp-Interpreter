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
    def test_execution_with_setf(self, mock_stdout):
        """
        Tests execution of code with setf
        :param mock_stdout:
        :return:
        """
        code = """
            (let ((x 10)
                  (y 20))
                (setf z (+ x y))
                (print z))
        """
        tokens = tokenize(code)
        execute_node_iterative(tokens)
        self.assertEqual(mock_stdout.getvalue().strip(), "30")

    @patch('sys.stdout', new_callable=StringIO)
    def test_execution_with_if_true(self, mock_stdout):
        """
        Tests execution of code with if (if condition is true)
        :param mock_stdout:
        :return:
        """
        code = """
            (let ((x 14))
            (if (evenp x)
              (print x)))
        """
        tokens = tokenize(code)
        execute_node_iterative(tokens)
        self.assertEqual(mock_stdout.getvalue().strip(), "14")

    @patch('sys.stdout', new_callable=StringIO)
    def test_execution_with_if_false(self, mock_stdout):
        """
        Tests execution of code with if (if condition is false)
        :param mock_stdout:
        :return:
        """
        code = """
            (let ((x 15))
            (if (evenp x)
              (print x)))
        """
        tokens = tokenize(code)
        execute_node_iterative(tokens)
        self.assertEqual(mock_stdout.getvalue().strip(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_execution_with_loop(self, mock_stdout):
        """
        Test s execution of code with loop
        :param mock_stdout:
        :return:
        """
        code = """
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
        """
        tokens = tokenize(code)
        execute_node_iterative(tokens)
        self.assertEqual(mock_stdout.getvalue().strip(), "25")

if __name__ == '__main__':
    unittest.main()
