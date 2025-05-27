from src.parser.node import Node
from src.executor.operations.operators import global_context

def _evaluate(node: Node, context=global_context):
    # pylint: disable=R0911,R1710
    if not node.tokens and not node.children:
        return None

    if node.tokens:
        first_token = node.tokens[0]

        if len(node.tokens) == 1 and not node.children:
            value = node.tokens[0]
            if isinstance(value, str):
                return context.find(value)[value]
            return value

        if isinstance(first_token, str):
            if first_token in {"setf", "loop", "if"}:
                return context.find(first_token)[first_token](node, context, _evaluate)
            if first_token == "let":
                return context.update(context.find(first_token)[first_token](node.children[0].children))

        func = context.find(first_token)[first_token]
        args = [_evaluate(child, context) for child in node.children]

        for token in node.tokens[1:]:
            if isinstance(token, str):
                args.append(context.find(token)[token])
            else:
                args.append(token)

        return func(*args)

    if node.children:
        result = None
        for child in node.children:
            result = _evaluate(child, context)
        return result

def execute_node_iterative(root: Node, context=global_context):
    result = None
    for child in root.children:
        result = _evaluate(child, context)
    return result