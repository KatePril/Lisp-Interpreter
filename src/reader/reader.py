"""
CLI entry point for the Lisp interpreter.
"""

import sys
from src.parser.parser import tokenize
from src.executor.executor import execute_node_iterative

def main():
    """Read a Lisp file, tokenize, execute, and print the result."""
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            source = f.read()
    else:
        print("You did not enter your filepath.")
        return
    node = tokenize(source)
    result = execute_node_iterative(node)
    print(result)