class aBST:
    def __init__(self, depth: int):
        self.tree_size = sum([2**(i) for i in range(depth+1)])
        self.Tree = [None] * self.tree_size

    def _find_key(self, i: int, key: int):
        if i > self.tree_size-1:
            return None
        if self.Tree[i] is None:
            return -i
        elif self.Tree[i] > key:
            return self._find_key(2*i + 1, key)
        elif self.Tree[i] < key:
            return self._find_key(2*i + 2, key)
        elif self.Tree[i] == key:
            return i

    def _add_key(self, i: int, key: int):
        if i > self.tree_size-1:
            return None
        if self.Tree[i] is None:
            self.Tree[i] = key
            return i
        elif self.Tree[i] > key:
            return self._add_key(2*i + 1, key)
        elif self.Tree[i] < key:
            return self._add_key(2*i + 2, key)
        elif self.Tree[i] == key:
            return -1
	
    def FindKeyIndex(self, key: int):
        if self.Tree[0] is None:
            return None
        return self._find_key(0, key)
	
    def AddKey(self, key: int):
        return self._add_key(0, key)


