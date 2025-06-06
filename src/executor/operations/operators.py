"""
Module defining Lisp-style operations and control flow for a interpreter.
"""

from typing import Any, Callable, Union

from src.executor.context import Context
from src.parser.node import Node


def add(*args: Union[int, float, str]) -> Union[int, float, str]:
    """
    Return the sum of all arguments. If any argument is a string, concatenate all as strings.
    """
    if any(isinstance(arg, str) for arg in args):
        return ' '.join(str(arg) for arg in args)
    result = 0
    for num in args:
        result += num
    return result


def sub(*args: Union[int, float]) -> Union[int, float]:
    """
    Return the result of sequential subtraction of arguments.
    """
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        result -= num
    return result


def mul(*args: Union[int, float]) -> Union[int, float]:
    """
    Return the product of all arguments.
    """
    result = 1
    for num in args:
        result *= num
    return result


def div(*args: Union[int, float]) -> Union[int, float]:
    """
    Return the result of sequential division of arguments.
    """
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        result /= num
    return result


def lisp_mod(number1: int, number2: int) -> int:
    """
    Return the modulo of two numbers.
    """
    return number1 % number2


def lisp_print(*args: Any) -> None:
    """
    Print all arguments separated by space.
    """
    print()
    for arg in args:
        print(arg, end=" ")


def equal(*args: Any) -> bool:
    """
    Check if all arguments are equal.
    """
    if not args:
        return True
    for i in range(len(args) - 1):
        if args[i] != args[i + 1]:
            return False
    return True


def is_more(value1: Union[int, float], value2: Union[int, float]) -> bool:
    """
    Return True if value1 > value2.
    """
    return value1 > value2


def is_less(value1: Union[int, float], value2: Union[int, float]) -> bool:
    """
    Return True if value1 < value2.
    """
    return value1 < value2


def lisp_if(node: Node, context: Context, evaluate: Callable) -> Any:
    """
    Evaluate a conditional expression with optional else branch.
    Handles multiline instructions by evaluating all children in the chosen branch.
    """
    condition = evaluate(node.children[0], context)
    if_context = Context(parent_context=context)
    results = []
    if condition:
        for child in node.children[1:]:
            results.append(evaluate(child, if_context))
    return results[-1] if results else None


def lisp_not(value: Any) -> bool:
    """
    Return the logical negation of a value.
    """
    return not value


def lisp_and(val1: bool, val2: bool) -> bool:
    """
    Return True if both values are True.
    """
    return val1 and val2


def lisp_or(val1: bool, val2: bool) -> bool:
    """
    Return True if at least one value is True.
    """
    return val1 or val2


def execute_let(nodes: list[Node]) -> dict:
    """
    Execute let-binding and return variable-value pairs.
    """
    return {node.tokens[0]: node.tokens[1][1:len(node.tokens[1])-1] if isinstance(node.tokens[1], str) else node.tokens[1] for node in nodes}


def execute_setf(node: Node, context: Context, evaluate: Callable) -> None:
    """
    Set variable in context to evaluated result.
    """
    variable = node.tokens[1]
    context[variable] = evaluate(node.children[0], context)


def execute_loop(node: Node, context: Context, evaluate: Callable) -> list[Any]:
    """
    Execute a loop with start, stop, and optional step.
    Handles multiline instructions by evaluating all children in the loop body.
    """
    start = int(node.tokens[4])
    stop = int(node.tokens[6])
    step = int(node.tokens[8]) if len(node.tokens) >= 9 else 1
    results = []
    for i in range(start, stop, step):
        context[node.tokens[2]] = i
        for child in node.children:
            results.append(evaluate(child, context))
    return results[-1] if results else None


KEYWORDS = {
    "+": add,
    "-": sub,
    "mul": mul,
    "div": div,
    "mod": lisp_mod,
    "print": lisp_print,
    "write": lisp_print,
    "=": equal,
    ">": is_more,
    "<": is_less,
    "let": execute_let,
    "setf": execute_setf,
    "loop": execute_loop,
    "if": lisp_if,
    "and": lisp_and,
    "or": lisp_or,
    "not": lisp_not,
    "evenp": lambda x: x % 2 == 0,
}

global_context = Context()
global_context.update(KEYWORDS)