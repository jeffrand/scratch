class HashTree(object):
    def __init__(self, *args, **kwargs):
        ''' A simple hash tree. args is a a tuple of strings '''
        self.tree = {}
        self.wildcard = str(kwargs.pop('wildcard', '*'))
        if args:
            for string in args:
                self.set(string)

    def set(self, string):
        ''' Store a string in the hash tree '''
        if not self.get(string):
            node = self.tree
            for i in string:
                if not node.has_key(i):
                    node[i] = {}
                node = node.get(i)

    def get(self, string):
        ''' Look in the hash tree for a string '''
        node = self.tree
        for i in string:
            if i == self.wildcard:
                return True
            elif not node.has_key(i):
                return False
            node = node.get(i)
        return True
