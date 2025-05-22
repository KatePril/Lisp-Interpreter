from functools import reduce
from math import sumprod

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

KEYWORDS = {
    "+": add,
    "-": sub,
    "print": lisp_print,
    "==": equal,
    ">": is_more,
    "<": is_less
}
