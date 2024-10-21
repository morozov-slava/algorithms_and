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

    # 2.* (бонус +500) Поиск наименьшего общего предка (LCA). 
    # Напишите метод, который находит наименьшего общего предка двух узлов в текущем дереве, представленном в виде массива. 
    # Объясните, как индексы в массиве могут быть использованы для упрощения поиска, по сравнению с классической рекурсивной реализацией.
    def _get_key_path(self, key: int):
        path = []
        i = 0
        while True:
            path.append(self.Tree[i])
            if self.Tree[i] == key:
                break
            elif self.Tree[i] > key:
                i = 2*i + 1
            elif self.Tree[i] < key:
                i = 2*i + 2
        return path
    
    def find_least_common_ancestor(self, key1: int, key2: int):
        k1_path = self._get_key_path(key1)
        k2_path = self._get_key_path(key2)
        lca = None
        for a, b in zip(k1_path, k2_path):
            if a == b:
                lca = a
            else:
                break
        return lca


