class Vertex:
    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:
    def __init__(self, size: int):
        self.max_vertex = size
        self.vertex = [None] * size 
        self.adjacency_list = {i: set() for i in range(size)} 

    def AddVertex(self, v: int):
        empty_index = None
        for i in range(len(self.vertex)):
            if self.vertex[i] is None:
                empty_index = i
                break
        if empty_index is not None:
            self.vertex[empty_index] = Vertex(v)

    def AddEdge(self, v1: int, v2: int):
        self.adjacency_list[v1].add(v2)
        self.adjacency_list[v2].add(v1)

    def IsEdge(self, v1: int, v2: int):
        return v1 in self.adjacency_list[v2]

    def GetSize(self):
        return self.max_vertex

    def IsEmptyVertex(self, index: int):
        return self.vertex[index] is None

    def GetTriangleNeighbours(self, index: int) -> set:
        triangle_neighbour_indices = set()
        for i in self.adjacency_list[index]:
            neighbour_nodes = self.adjacency_list[index].intersection(self.adjacency_list[i])
            if len(neighbour_nodes):
                triangle_neighbour_indices = triangle_neighbour_indices.union(neighbour_nodes)
        return triangle_neighbour_indices


# 2.* Реализуйте метод поиска узлов, не входящих ни в один треугольник в графе, только через интерфейс класса (операции над графом).
def get_weak_vertices(Graph: SimpleGraph) -> list:
    beyond_triangle_indices = []
    triangle_indices = set()
    for i in range(Graph.GetSize()):
        if (Graph.IsEmptyVertex(i)) or (i in triangle_indices):
            continue
        triangle_neighbours = Graph.GetTriangleNeighbours(i)
        if len(triangle_neighbours):
            triangle_indices = triangle_indices.union(triangle_neighbours)
            continue
        beyond_triangle_indices.append(i)  
    return beyond_triangle_indices


