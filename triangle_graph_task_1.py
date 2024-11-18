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

    # 1.* Добавьте метод, подсчитывающий общее число треугольников в графе.
    def get_total_number_of_triangles(self):
        for Node in self.vertex:
            if (Node is None) or (Node.Hit == False):
                continue
            Node.Hit = False
        if self.vertex[0] is None:
            return 0
        return self._get_triangle_node(0, 0)
        
    def _get_triangle_node(self, index, n_triangles: int):
        if index == self.max_vertex:
            return n_triangles
        self.vertex[index].Hit = True
        connected_nodes = []
        for i in range(self.max_vertex):
            if self.vertex[i] is None:
                continue
            if (self.m_adjacency[index][i] == 1) and (self.vertex[i].Hit == False):
                connected_nodes.append(i)
        if len(connected_nodes) <= 1:
            return self._get_triangle_node(index+1, n_triangles)
        # check connected nodes for triangle
        for j in range(len(connected_nodes)-1):
            v1 = connected_nodes[j]
            v2 = connected_nodes[j+1]
            if (self.m_adjacency[index][v1] == 1) and (self.m_adjacency[index][v2] == 1) and (self.m_adjacency[v1][v2] == 1):
                n_triangles += 1
        return self._get_triangle_node(index+1, n_triangles)


