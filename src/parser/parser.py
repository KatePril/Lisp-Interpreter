from Node import Node

KEYWORDS = {
  'let'
}

def toParts(source: str) -> list[str]:
  parts = source.replace(')', ' ) ').replace('(', ' ( ').strip().split()
  result = []
  stack = []
  level = 0
  for part in parts:
    if part in KEYWORDS:
      result.append('(')
      stack.append(level + 1)
      level += 1
    if part == '(':
      level += 1
    elif part == ')':
      level -= 1
    result.append(part)
    if len(stack) > 0 and stack[-1] == level and part == ')':
      result.append(')')
  return result

def tokenize(source: str) -> Node:
  parts = toParts(source)
  root = current = Node()
  for part in parts:
    if part == '(':
      node = Node(current)
      current.childs.append(node)
      current = node
    elif part == ')':
      current = current.parent
    else:  
      current.tokens.append(part)
  return root.childs[0]
