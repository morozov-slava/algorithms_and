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

    def EvenTrees(self):
        n_descendants, edges_to_delete = self._even_tree_splitter(self.Root)
        return edges_to_delete

    def _even_tree_splitter(self, Node: SimpleTreeNode):
        edges_to_delete = []
        n_descendants = 1
        for ChildNode in Node.Children:
            child_n_descendants, child_edges_to_delete = self._even_tree_splitter(ChildNode)
            n_descendants += child_n_descendants
            edges_to_delete.extend(child_edges_to_delete)
        if (n_descendants % 2 == 0) and (self.Root != Node):
            edges_to_delete.append(Node.Parent)
            edges_to_delete.append(Node)
            n_descendants = 0
        return n_descendants, edges_to_delete

    # 3.* (бонус +500) Добавьте метод, который для текущего дерева определяет общее количество чётных поддеревьев. 
    def CountEvenSubtree(self):
        return self._count_even_subtree(self.Root, 1)

    def _count_even_subtree(self, Node: SimpleTreeNode, nodes_counter: int):
        n_even_subtrees = 0
        if nodes_counter % 2 == 0:
            n_even_subtrees = 1
        for ChildNode in Node.Children:
            n_even_subtrees += self._count_even_subtree(ChildNode, nodes_counter+1)
            n_even_subtrees += self._count_even_subtree(ChildNode, 1) 
        return n_even_subtrees


