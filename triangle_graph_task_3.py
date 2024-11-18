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

    # 3.* (бонус +500) Когда в графе число рёбер близко к максимальному, полезно использовать достаточно эффективный алгоритм поиска узлов, 
    #                  не входящих ни в один треугольник в графе, который анализирует матрицу смежности
    def get_beyond_triangle_nodes(self):
        beyond_triangle_indices = []
        triangle_indices = set()
        for i in range(self.max_vertex):
            if i in triangle_indices:
                continue
            connected_indices = []
            for j in range(self.max_vertex):
                if self.m_adjacency[i][j] == 1:
                    connected_indices.append(j)
            if len(connected_indices) <= 1:
                beyond_triangle_indices.append(i)
                continue
            is_triangle_index = False
            for ci in range(len(connected_indices)-1):
                v1 = connected_indices[ci]
                v2 = connected_indices[ci+1]
                if self.m_adjacency[v1][v2] == 1:
                    if not is_triangle_index:
                        is_triangle_index = True
                    triangle_indices.add(v1)
                    triangle_indices.add(v2)
            if is_triangle_index:
                triangle_indices.add(i)
                continue
            beyond_triangle_indices.append(i)
        return beyond_triangle_indices


