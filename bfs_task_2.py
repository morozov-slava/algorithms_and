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



class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []
	
class SimpleTree:
    def __init__(self, root):
        self.Root = root

    def _get_all_nodes(self, StartNode):
        all_nodes = [StartNode]
        for N in StartNode.Children:
            if len(N.Children):
                all_nodes.extend(self._get_all_nodes(N))
            else:
                all_nodes.append(N)
        return all_nodes

    def _get_node_by_value(self, StartNode, value):
        nodes = []
        if StartNode.NodeValue == value:
            nodes.append(StartNode)
        for N in StartNode.Children:
            nodes.extend(self._get_node_by_value(N, value))
        return nodes

    def _get_number_of_nodes(self, StartNode):
        n_nodes = 1
        for N in StartNode.Children:
            n_nodes += self._get_number_of_nodes(N)
        return n_nodes

    def _get_number_of_leaves(self, StartNode):
        n_leaves = 0
        if len(StartNode.Children) == 0:
            n_leaves += 1
            return n_leaves
        for N in StartNode.Children:
            n_leaves += self._get_number_of_leaves(N)
        return n_leaves
	
    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode
  
    def DeleteNode(self, NodeToDelete):
        parent_node = NodeToDelete.Parent
        parent_node.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None
        
    def GetAllNodes(self):
        return self._get_all_nodes(self.Root)

    def FindNodesByValue(self, val):
        return self._get_node_by_value(self.Root, val)
   
    def MoveNode(self, OriginalNode, NewParent):
        self.DeleteNode(OriginalNode)
        NewParent.Children.append(OriginalNode)
        OriginalNode.Parent = NewParent
   
    def Count(self):
        return self._get_number_of_nodes(self.Root)

    def LeafCount(self):
        return self._get_number_of_leaves(self.Root)

    # 2.* Используя BFS, найдите два наиболее удалённых друг от друга узла в обычном дереве, 
    #     которое теперь воспринимаем как граф, и возвращайте это максимальное расстояние. 
    def FindMaxNodesDistance(self):
        if self.Root is None:
            return 0
        queue = Queue()
        queue.enqueue(Node((self.Root, 0)))
        max_distance = 0
        farthest_node = self.Root
        while not queue.is_empty():
            node, distance = queue.dequeue().value
            for child in node.Children:
                queue.enqueue(Node((child, distance+1)))
                if distance + 1 > max_distance:
                    max_distance = distance + 1
                    farthest_node = child
        return max_distance


