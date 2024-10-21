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

    # 3. (бонус +500) Переделайте метод обход дерева в ширину, оптимизируя его за счёт прямого доступа к элементам массива.
    def WideAllNodes(self):
        return self._wide_node(self.Tree, 0, 0)

    def _wide_node(self, array: list, start_index: int, current_level: int):
        current_level_nodes = []
        if start_index >= self.tree_size - 1:
            return []
        n_nodes_on_level = 2**current_level
        for i in range(start_index, start_index+n_nodes_on_level):
            if array[i] is not None:
                current_level_nodes.append(array[i])
        current_level_nodes.extend(
            self._wide_node(array, start_index+n_nodes_on_level, current_level+1)
        )
        return current_level_nodes


