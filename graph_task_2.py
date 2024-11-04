class Vertex:
    def __init__(self, val):
        self.Value = val
  
class DirectedGraph:
    def __init__(self, size: int):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size
        
    def AddVertex(self, v: int):
        empty_index = None
        for i in range(len(self.vertex)):
            if self.vertex[i] is None:
                empty_index = i
                break
        if empty_index is not None:
            self.vertex[empty_index] = Vertex(v)

    def RemoveVertex(self, v: int):
        if self.vertex[v] is not None:
            self.vertex[v] = None
        # remove edges
        for i in range(self.max_vertex):
            if self.m_adjacency[v][i] != 0:
                self.m_adjacency[v][i] = 0
            if self.m_adjacency[i][v] != 0:
                self.m_adjacency[i][v] = 0 
	
    def IsEdge(self, v1: int, v2: int):
        if (self.m_adjacency[v1] is None) or (self.m_adjacency[v2] is None):
            return False
        return bool(self.m_adjacency[v1][v2])
	
    def AddEdge(self, parent_v: int, child_v: int):
        if (self.m_adjacency[parent_v] is not None) or (self.m_adjacency[child_v] is not None):
            self.m_adjacency[parent_v][child_v] = 1
	
    def RemoveEdge(self, parent_v: int, child_v: int):
        if (self.m_adjacency[parent_v] is not None) and (self.m_adjacency[child_v] is not None):
            self.m_adjacency[parent_v][child_v] = 0

    # 2.* (бонус +500) Реализуйте направленный граф, представленный матрицей смежности, и добавьте метод проверки, будет ли он циклическим. 
    def IsCyclic(self):
        if self.max_vertex == 0:
            return False
        return self._is_cyclic_path(0, [self.vertex[0].Value])

    def _is_cyclic_path(self, parent_index: int, current_path: list):
        if parent_index >= self.max_vertex:
            return False
        for i in range(self.max_vertex):
            if (self.vertex[i] is None) or (self.m_adjacency[parent_index][i] == 0):
                continue
            if (self.m_adjacency[parent_index][i] == 1) and (self.vertex[i].Value in current_path):
                return True
            return self._is_cyclic_path(i, current_path + [self.vertex[i].Value])
        return False


