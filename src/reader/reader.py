import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.parser.parser import tokenize
from src.executor.operations.operators import global_context
from src.executor.executor import execute_node_iterative


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            source = f.read()
    else:
        print("You did not enter your filepath.")
        return
    node = tokenize(source)
    print(node)
    result = execute_node_iterative(node)
    print(result)

if __name__ == "__main__":
    main()