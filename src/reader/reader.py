"""
CLI entry point for the Lisp interpreter.
"""

import sys
import os
from src.parser.parser import tokenize
from src.executor.executor import execute_node_iterative

def main():
    """Read a Lisp file, tokenize, execute, and print the result."""
    if len(sys.argv) > 1:
        if not os.path.isfile(sys.argv[1]):
            print("File was not found.")
            return
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            source = f.read()
            node = tokenize(source)
            execute_node_iterative(node)
    else:
        print("You did not enter your filepath.")
        return