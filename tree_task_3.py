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

# Задание 3. * (бонус +500) Добавьте метод проверки, симметрично ли дерево относительно своего корня. 
def is_symmetric_level(one_level_nodes: list):
    n_children_nodes = None
    next_level_nodes = []
    for Node in one_level_nodes:
        next_level_nodes.extend(Node.Children)
        if n_children_nodes is None:
            n_children_nodes = len(Node.Children)
        if n_children_nodes != len(Node.Children):
            return False
    if len(next_level_nodes):
        return is_symmetric_level(next_level_nodes)
    return True

def is_symmetric_tree(Tree: SimpleTree):
    return is_symmetric_level(Tree.Root.Children)


