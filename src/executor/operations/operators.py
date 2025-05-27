from context import Context
from src.parser import Node


def add(*args):
    result = 0
    for num in args:
        result += num
    return result

def sub(*args):
    if len(args) < 1:
        return 0
    result = args[0]
    for i in range(len(args) - 1):
        result -= args[i + 1]
    return result

def mul(*args):
    result = 1
    for num in args:
        result *= num
    return result

def div(*args):
    if len(args) < 1:
        return 0
    result = args[0]
    for i in range(len(args) - 1):
        result /= args[i + 1]
    return result

def lisp_mod(number1, number2):
    return number1 % number2

def lisp_print(*args):
    for arg in args:
        print(arg, end=" ")

def equal(*args):
    if len(args) < 1:
        return True
    for i in range(len(args) - 1):
        if args[i] != args[i + 1]:
            return False
    return True

def is_more(value1, value2):
    if value1 > value2:
        return True
    return False

def is_less(value1, value2):
    if value1 < value2:
        return True
    return False

def lisp_if(node: Node, context: Context, evaluate):
    condition = evaluate(node.children[0], context)
    if condition:
        return evaluate(node.children[1], context)
    elif len(node.children) > 2:
        return evaluate(node.children[2], context)
    else:
        return None

def lisp_not(value):
    return not value

def lisp_and(val1: bool, val2: bool):
    if val1 == val2 == True:
        return True
    return False

def lisp_or(val1: bool, val2: bool):
    if val1 or val2:
        return True
    return False

def execute_let(nodes: list[Node]):
    return {node.tokens[0]: node.tokens[1] for node in nodes}

def execute_setf(node: Node, context: Context, evaluate: function):
    variable = node.tokens[1]
    context[variable] = evaluate(node.children[0], context)

def execute_loop(node: Node, context: Context, evaluate: function):
    start, stop = int(node.tokens[4]), int(node.tokens[6])
    step = node.tokens[8] if len(node.tokens) >= 9 else 1
    for i in range(start, stop, step):
        context.update({node.tokens[2]: i})
        loop_context = Context(parent_context=context)
        evaluate(node.children[0], loop_context)


KEYWORDS = {
    "+": add,
    "-": sub,
    "mul": mul,
    "div": div,
    "mod": lisp_mod,
    "print": lisp_print,
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
}
