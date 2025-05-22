"""This module provides code for"""
import unittest
from src.parser.parser import tokenize


class TestParser(unittest.TestCase):
    """
    This class tests if the parser parses Lisp code correctly
    """
    def setUp(self):
        self.source_one = """
            (
                let (
                    (x 25)
                    (y 30)
                )
                (write (+ x y))
            )
        """
        self.source_two = """
            (
                let (
                    (sum 0)
                )
                (loop for i from 1 to 10 do
                    (
                        setf sum (+ sum i)
                    )
                )
                (print sum)
            )
        """
    def test_with_source_one(self):
        """
        Tests if the parser parses first example of Lisp code correctly
        :return:
        """
        node = tokenize(self.source_one)
        self.assertEqual(len(node.children), 2)
        self.assertEqual(len(node.tokens), 0)

        self.assertEqual(len(node.children[0].children), 1)
        self.assertEqual(node.children[0].tokens[0], "let")
        self.assertEqual(len(node.children[0].children[0].children), 2)
        self.assertEqual(
            node.children[0].children[0].children[0].tokens,
            ["x", "25"]
        )
        self.assertEqual(
            node.children[0].children[0].children[1].tokens,
            ["y", "30"]
        )

        self.assertEqual(len(node.children[1].children), 1)
        self.assertEqual(node.children[1].tokens[0], "write")
        self.assertEqual(len(node.children[1].children), 1)
        self.assertEqual(node.children[1].children[0].tokens, ["+", "x", "y"])

    def test_with_source_two(self):
        """
        Tests if the parser parses second example of Lisp code correctly
        :return:
        """
        node = tokenize(self.source_two)

        self.assertEqual(len(node.children), 3)
        self.assertEqual(len(node.tokens), 0)
        self.assertEqual(len(node.children[0].children), 1)

        self.assertEqual(len(node.children[0].children[0].children), 1)
        self.assertEqual(
            node.children[0].children[0].children[0].tokens,
            ['sum', '0']
        )

        self.assertEqual(
            node.children[1].tokens,
            ['loop', 'for', 'i', 'from', '1', 'to', '10', 'do']
        )
        self.assertEqual(len(node.children[1].children), 1)
        self.assertEqual(
            node.children[1].children[0].tokens,
            ['setf', 'sum']
        )
        self.assertEqual(len(node.children[1].children[0].children), 1)
        self.assertEqual(
            node.children[1].children[0].children[0].tokens,
            ['+', 'sum', 'i']
        )

        self.assertEqual(len(node.children[2].children), 0)
        self.assertEqual(node.children[2].tokens, ["print", "sum"])




if __name__ == '__main__':
    unittest.main()
