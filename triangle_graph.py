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
        if self.vertex[0] is None:
            return []
        triangle_indices = list(self._weak_vertices([(0, None, set())], set()))
        beyond_triangle_nodes = [self.vertex[i] for i in range(self.max_vertex) if (self.vertex[i] is not None) and i not in triangle_indices]
        return beyond_triangle_nodes

    def _weak_vertices(self, queue: list, triangle_indices: set):
        if len(queue) == 0:
            return triangle_indices
        index, prev_index, prev_node_connected_indices = queue.pop(0)
        self.vertex[index].Hit = True
        connected_visited_nodes = set()
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                continue
            if self.m_adjacency[index][i] == 1:
                connected_visited_nodes.add(i)
        for ci in connected_visited_nodes:
            if self.vertex[ci].Hit == False:
                queue.append((ci, index, connected_visited_nodes))
        intersected_indices = connected_visited_nodes.intersection(prev_node_connected_indices)
        if len(intersected_indices):
            triangle_indices.add(prev_index)
            triangle_indices.add(index)
        return self._weak_vertices(queue, triangle_indices)


