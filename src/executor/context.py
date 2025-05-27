"""
This module contains Context class
"""

class Context(dict):
    """
    Context with variables and functions definitions.
    """

    def __init__(self, params=(), args=(), parent_context=None):
        """
        Constructor.
        :param params: variables names
        :param args: variables definitions
        :param parent_context: the link to the parent context
        """
        super().__init__()
        self.update(zip(params, args))
        self.parent_context = parent_context

    def find(self, name):
        """
        Returns variable definition by name.
        :param name: variable name
        :return:
        """
        if name in self:
            return self
        if self.parent_context:
            return self.parent_context.find(name)
        raise NameError(f"Undefined variable: {name}")