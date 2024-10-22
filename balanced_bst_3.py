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
            return -1
        if self.Tree[i] is None:
            self.Tree[i] = key
            return i
        elif self.Tree[i] > key:
            return self._add_key(2*i + 1, key)
        elif self.Tree[i] < key:
            return self._add_key(2*i + 2, key)
        elif self.Tree[i] == key:
            return i
	
    def FindKeyIndex(self, key: int):
        if self.Tree[0] is None:
            return None
        return self._find_key(0, key)
	
    def AddKey(self, key: int):
        return self._add_key(0, key)

    # 3.* (бонус +500) Реализуйте метод удаления узла из двоичного дерева, заданного в виде массива. Несмотря на отсутствие пустых мест, метод должен корректно перестраивать дерево, сохраняя балансировку.
    def DeleteKey(self, key: int):
        index = self.FindKeyIndex(key)
        if index is None:
            return False
        self.Tree[index] = None
        if len(self.Tree):
            a = sorted([x for x in self.Tree if x is not None])
            bbst_array = self._rebalance_bst([a])
            bbst_array = bbst_array + [None] * (self.tree_size - len(bbst_array))
            self.Tree = bbst_array
        return True

    def _rebalance_bst(self, one_level_arrays: list):
        balanced_bst_array = []
        next_level_arrays = []
        for array in one_level_arrays:
            if len(array):
                mid_i = len(array) // 2
                balanced_bst_array.append(array[mid_i])
            if len(array) > 2: 
                next_level_arrays.append(array[:mid_i])
                next_level_arrays.append(array[mid_i+1:])
            elif len(array) == 2:
                next_level_arrays.append(array[:mid_i])
        if len(next_level_arrays):
            balanced_bst_array.extend(
                self._rebalance_bst(next_level_arrays)
            )
        return balanced_bst_array


