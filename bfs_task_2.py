class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def dequeue(self):
        if self.head is None:
            return None
        old_head = self.head
        new_head = self.head.next
        self.head = new_head
        return old_head

    def is_empty(self):
        return self.head is None


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
    
    # 2.* Используя BFS, найдите два наиболее удалённых друг от друга узла в обычном дереве, 
    #     которое теперь воспринимаем как граф, и возвращайте это максимальное расстояние.
    def FindMaxNodesDistance(self):
        if self.vertex[0] is None:
            return 0
        first_farthest_node_index, _ = self._one_node_bfs(0)
        _, max_distance = self._one_node_bfs(first_farthest_node_index)
        return max_distance
    
    def _one_node_bfs(self, start_node_index: int):
        queue = Queue()
        queue.enqueue(Node((start_node_index, 0)))
        visited_indices = [None] * self.max_vertex
        max_distance = 0
        farthest_node_index = start_node_index
        while not queue.is_empty():
            index, distance = queue.dequeue().value
            visited_indices[index] = 1
            if distance > max_distance:
                max_distance = distance
                farthest_node_index = index
            for i in range(self.max_vertex):
                if self.m_adjacency[index][i] == 1 and visited_indices[i] is None:
                    queue.enqueue(Node((i, distance+1)))
        return farthest_node_index, max_distance


