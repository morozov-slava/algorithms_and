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

    def WeakVertices(self):
        for Node in self.vertex:
            if (Node is None) or (Node.Hit == False):
                continue
            Node.Hit = False
        return self._weak_vertices([0], [])

    def _weak_vertices(self, queue: list, beyond_triangle_nodes: list):
        if len(queue) == 0:
            return beyond_triangle_nodes
        index = queue.pop(0)
        self.vertex[index].Hit = True
        connected_visited_nodes = []
        for i in range(self.max_vertex):
            if (self.vertex[i] is None):
                continue
            if (self.m_adjacency[index][i] == 1) and (self.vertex[i].Hit == True):
                connected_visited_nodes.append(i)
            if (self.m_adjacency[index][i] == 1) and (self.vertex[i].Hit == False) and (i not in queue):
                queue.append(i)
        if len(connected_visited_nodes) >= 2:
            for n in connected_visited_nodes:
                if self.vertex[n] in beyond_triangle_nodes:
                    beyond_triangle_nodes.remove(self.vertex[n])
        if len(connected_visited_nodes) < 2:
            beyond_triangle_nodes.append(self.vertex[index])
        return self._weak_vertices(queue, beyond_triangle_nodes)


