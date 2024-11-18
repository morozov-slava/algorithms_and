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

    # 2.* (бонус +500) В ориентированном графе найдите длину самого длинного простого пути (пути без повторяющихся вершин). 
    #      Граф может содержать циклы, и вам нужно игнорировать их при поиске. 
    def GetLongestEasyWay(self):
        if self.max_vertex == 0:
            return 0
        return self._find_longest_easy_way(0, 0, set())

    def _find_longest_easy_way(self, index: int, depth: int, visited_nodes: set):
        visited_nodes.add(index)
        max_depth = depth
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                continue
            if (self.m_adjacency[index][i] == 1) and (i not in visited_nodes):
                neighbour_depth = self._find_longest_easy_way(i, depth+1, visited_nodes)
                if neighbour_depth > max_depth:
                    max_depth = neighbour_depth
        return max_depth


