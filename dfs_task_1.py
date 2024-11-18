class Vertex:
    def __init__(self, val):
        self.Value = val
        self.Hit = False
  
class SimpleGraph:
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
        return bool(self.m_adjacency[v1][v2]) and bool(self.m_adjacency[v2][v1])
	
    def AddEdge(self, v1: int, v2: int):
        if (self.m_adjacency[v1] is not None) or (self.m_adjacency[v2] is not None):
            self.m_adjacency[v1][v2] = 1
            self.m_adjacency[v2][v1] = 1
	
    def RemoveEdge(self, v1: int, v2: int):
        if (self.m_adjacency[v1] is not None) and (self.m_adjacency[v2] is not None):
            self.m_adjacency[v1][v2] = 0
            self.m_adjacency[v2][v1] = 0

    def DepthFirstSearch(self, VFrom: int, VTo: int):
        for Node in self.vertex:
            if (Node is None) or (Node.Hit == False):
                continue
            Node.Hit = False
        return self._depth_first_search(VFrom, VTo)

    def _depth_first_search(self, VFrom: int, VTo: int):
        self.vertex[VFrom].Hit = True
        path = [self.vertex[VFrom]]
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                continue
            if (self.m_adjacency[VFrom][i] == 1) and (i == VTo):
                path.append(self.vertex[i])
                return path
            if (self.m_adjacency[VFrom][i] == 1) and (self.vertex[i].Hit == False):
                path.extend(self._depth_first_search(i, VTo))
                if path[-1] == self.vertex[VTo]:
                    break
        if path[-1] != self.vertex[VTo]:
            return []
        return path

    # 1.* Добавьте метод, проверяющий, будет ли текущий неориентированный граф связным. Используйте для этого DFS.
    def IsConnectedGraph(self):
        for Node in self.vertex:
            if (Node is None) or (Node.Hit == False):
                continue
            Node.Hit = False
        return self._is_connected_graph(0, None)

    def _is_connected_graph(self, index: int, parent_index: int):
        self.vertex[index].Hit = True
        path = [index]
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                continue
            if (self.m_adjacency[index][i] == 1) and (self.vertex[i].Hit == True) and (i != parent_index):
                return True
            if (self.m_adjacency[index][i] == 1) and (self.vertex[i].Hit == False):
                connected_path = self._is_connected_graph(i, index)
                if connected_path == True:
                    return True
        return False


