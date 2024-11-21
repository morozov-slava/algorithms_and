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

    # 3.* (бонус +500) Когда в графе число рёбер близко к максимальному, полезно использовать достаточно эффективный алгоритм поиска узлов, 
    #                  не входящих ни в один треугольник в графе, который анализирует матрицу смежности.
    #                  Реализуйте такой алгоритм, и оцените его сложность (O-большое).
    def get_beyond_triangle_nodes(self):
        beyond_triangle_indices = []
        for i in range(self.max_vertex):
            is_triangle_index = False
            for j in self.adjacency_list[i]:
                intersected_nodes = self.adjacency_list[i].intersection(self.adjacency_list[j])
                if len(intersected_nodes):
                    is_triangle_index = True
                    break
            if not is_triangle_index:
                beyond_triangle_indices.append(i)
        return beyond_triangle_indices


