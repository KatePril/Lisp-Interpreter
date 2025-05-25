class Context(dict):
    def __int__(self, params=(), args=(), parent_context=None):
        self.update(zip(params, args))
        self.parent_context = parent_context

    def find(self, name):
        return self if name in self.keys() else self.parent_context.find(name)