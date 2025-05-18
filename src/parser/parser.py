from src.parser.Node import Node
from typing import Generator

KEYWORDS = {
  'let'
}

def _to_parts(source: str) -> Generator[str, None, None]:
  parts = source.replace(')', ' ) ').replace('(', ' ( ').strip().split()
  stack = []
  level = 0
  for part in parts:
    if part in KEYWORDS:
      stack.append(level + 1)
      level += 1
      yield '('
    if part == '(':
      level += 1
    elif part == ')':
      level -= 1
    yield part
    if len(stack) > 0 and stack[-1] == level and part == ')':
      stack.pop()
      yield ')'

def tokenize(source: str) -> Node:
  root = current = Node()
  for part in _to_parts(source):
    if part == '(':
      node = Node(current)
      current.children.append(node)
      current = node
    elif part == ')':
      current = current.parent
    else:
      current.tokens.append(part)
  return root.children[0]
