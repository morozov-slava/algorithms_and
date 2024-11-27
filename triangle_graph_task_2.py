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

    # 2.* Реализуйте метод поиска узлов, не входящих ни в один треугольник в графе, только через интерфейс класса (операции над графом).
    def WeakVertices(self):
        beyond_triangle_indices = []
        triangle_indices = [None] * self.max_vertex
        for i in range(self.max_vertex):
            if triangle_indices[i] is not None:
                continue
            is_triangle_index = False
            for j in self.adjacency_list[i]:
                if is_triangle_index is True:
                    break
                for k in self.adjacency_list[j]:
                    if self.IsEdge(k, i) and k != i:
                        is_triangle_index = True
                        triangle_indices[j] = True
                        triangle_indices[k] = True
                        break
            if not is_triangle_index:
                beyond_triangle_indices.append(i)
        return beyond_triangle_indices


