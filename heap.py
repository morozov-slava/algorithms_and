class Heap:
    def __init__(self):
        self.HeapArray = []
        self.HeapSize = 0

    def _clean_heap(self):
        if len(self.HeapArray):
            self.HeapArray = []

    def _rebalance_heap_up(self, start_index: int):
        if start_index == 0:
            return True
        parent_index = (start_index - 1) // 2
        parent_key = self.HeapArray[parent_index]
        current_key = self.HeapArray[start_index]
        if parent_key < current_key:
            self.HeapArray[parent_index] = current_key
            self.HeapArray[start_index] = parent_key
            return self._rebalance_heap_up(parent_index)
        return True

    def _rebalance_heap_down(self, start_index: int):
        if start_index > len(self.HeapArray):
            return True
        lc_i = 2*start_index + 1 # left child index
        rc_i = 2*start_index + 2 # right child index
        left_child_key = None
        right_child_key = None
        if lc_i < len(self.HeapArray):
            left_child_key = self.HeapArray[lc_i]
        if rc_i < len(self.HeapArray):
            right_child_key = self.HeapArray[rc_i]
        if (left_child_key is None) and (right_child_key is None):
            return True
        if (left_child_key is not None) and (right_child_key is None):
            max_key_child = left_child_key
            max_key_index = lc_i
        elif (left_child_key is None) and (right_child_key is not None):
            max_key_child = right_child_key
            max_key_index = rc_i
        elif (left_child_key is not None) and (right_child_key is not None):
            if left_child_key > right_child_key:
                max_key_child = left_child_key
                max_key_index = lc_i
            else:
                max_key_child = right_child_key
                max_key_index = rc_i
        current_key = self.HeapArray[start_index]
        if current_key < max_key_child:
            self.HeapArray[start_index] = max_key_child
            self.HeapArray[max_key_index] = current_key
            self._rebalance_heap_down(max_key_index)
        return True
		
    def MakeHeap(self, a: list, depth: int):
        self._clean_heap()
        heap_size = sum([2**(i) for i in range(depth+1)])
        if heap_size < len(a):
            raise KeyError("Given depth is higher than array lenght")
        self.HeapSize = heap_size
        for key in a[:heap_size]:
            self.Add(key)

    def GetMax(self):
        if len(self.HeapArray) == 0:
            return -1
        root = self.HeapArray.pop(0)
        if len(self.HeapArray):
            self.HeapArray.insert(0, self.HeapArray[-1])
            self.HeapArray.pop()
            self._rebalance_heap_down(0)
        return root

    def Add(self, key):
        if self.HeapSize > len(self.HeapArray):
            self.HeapArray.append(key)
            return self._rebalance_heap_up(len(self.HeapArray)-1)
        return False


