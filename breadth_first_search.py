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

    def BreadthFirstSearch(self, VFrom, VTo):
        for Node in self.vertex:
            if (Node is None) or (Node.Hit == False):
                continue
            Node.Hit = False
        path, NeighboursIndex = self._breadth_first_search(VTo, [(VFrom, None)])
        return path[::-1]

    def _breadth_first_search(self, VTo, queue: list):
        if len(queue) == 0:
            return []
        VFrom, NearestV = queue.pop(0)
        self.vertex[VFrom].Hit = True
        if VFrom == VTo:
            return [self.vertex[VFrom]], NearestV
        connected_i = []
        for i in range(self.max_vertex):
            if (self.m_adjacency[VFrom][i] == 1) and (self.vertex[i].Hit == False):
                connected_i.append((i, VFrom))
        queue.extend(connected_i)
        path, NearestNeighbourIndex = self._breadth_first_search(VTo, queue)
        if NearestNeighbourIndex != VFrom:
            return path, NearestNeighbourIndex
        path.append(self.vertex[VFrom])
        return path, NearestV


