class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        

class BSTFind:
    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False


class BST:
    def __init__(self, node):
        self.Root = node

    def _number_nodes_in_tree(self, Node: BSTNode):
        n_nodes = 1
        if Node.LeftChild is not None:
            n_nodes += self._number_nodes_in_tree(Node.LeftChild)
        if Node.RightChild is not None:
            n_nodes += self._number_nodes_in_tree(Node.RightChild)
        return n_nodes

    def _find_max_key_node(self, FromNode):
        if FromNode.RightChild is None:
            return FromNode
        return self._find_max_key_node(FromNode.RightChild)
            
    def _find_min_key_node(self, FromNode):
        if FromNode.LeftChild is None:
            return FromNode
        return self._find_min_key_node(FromNode.LeftChild)

    def _find_node_by_key(self, Node, key):
        if Node.NodeKey == key:
            return Node, True, False
        if (Node.NodeKey < key) and (Node.RightChild is None):
            return Node, False, False
        if (Node.NodeKey > key) and (Node.LeftChild is None):
            return Node, False, True
        if Node.NodeKey < key:
            return self._find_node_by_key(Node.RightChild, key) 
        return self._find_node_by_key(Node.LeftChild, key)

    def _add_key_value(self, Node, key, value):
        if Node.NodeKey == key:
            return False
        if (Node.NodeKey < key) and (Node.RightChild is None):
            Node.RightChild = BSTNode(key, value, Node)
            return True
        if (Node.NodeKey > key) and (Node.LeftChild is None):
            Node.LeftChild = BSTNode(key, value, Node)
            return True
        if Node.NodeKey < key:
            return self._add_key_value(Node.RightChild, key, value) 
        return self._add_key_value(Node.LeftChild, key, value)

    def _replace_node(self, NodeToReplace, ReplacingNode):
        parent_node = NodeToReplace.Parent
        if parent_node.NodeKey > NodeToReplace.NodeKey:
            parent_node.LeftChild = ReplacingNode
        else:
            parent_node.RightChild = ReplacingNode
        ReplacingNode.Parent = parent_node
        if NodeToReplace.LeftChild is not None:
            ReplacingNode.LeftChild = NodeToReplace.LeftChild
            NodeToReplace.LeftChild = None
        if NodeToReplace.RightChild is not None:
            ReplacingNode.RightChild = NodeToReplace.RightChild
            NodeToReplace.RightChild = None   

    def _replace_root_node(self, ReplacingNode):
        if self.Root.LeftChild is not None:
            ReplacingNode.LeftChild = self.Root.LeftChild
            ReplacingNode.LeftChild.Parent = ReplacingNode
            self.Root.LeftChild = None
        if self.Root.RightChild is not None:
            ReplacingNode.RightChild = self.Root.RightChild
            ReplacingNode.RightChild.Parent = ReplacingNode
            self.Root.RightChild = None
        self.Root = ReplacingNode
        
    def FindNodeByKey(self, key):
        Node, NodeHasKey, ToLeft = self._find_node_by_key(self.Root, key)
        bst_find = BSTFind()
        bst_find.Node = Node
        bst_find.NodeHasKey = NodeHasKey
        bst_find.ToLeft = ToLeft
        return bst_find

    def AddKeyValue(self, key, val):
        if self.Root is None:
            self.Root = BSTNode(key, val, parent=None)
            return True
        return self._add_key_value(self.Root, key, val)
  
    def FinMinMax(self, FromNode, FindMax: bool):
        if FindMax:
            return self._find_max_key_node(FromNode)
        return self._find_min_key_node(FromNode)
	
    def DeleteNodeByKey(self, key):
        bst_find = self.FindNodeByKey(key)
        if not bst_find.NodeHasKey:
            return bst_find.NodeHasKey 
        if bst_find.Node == self.Root:
            if (bst_find.Node.RightChild is None) and (bst_find.Node.LeftChild is None):
                self.Root = None
                return bst_find.NodeHasKey 
            elif (bst_find.Node.RightChild is not None):
                ReplacingNode = self.FinMinMax(bst_find.Node.RightChild, FindMax=False)
            else:
                ReplacingNode = self.FinMinMax(bst_find.Node.LeftChild, FindMax=False)
            self.DeleteNodeByKey(ReplacingNode.NodeKey)
            self._replace_root_node(ReplacingNode)
            return bst_find.NodeHasKey
        if (bst_find.Node.LeftChild is None) and (bst_find.Node.RightChild is None):
            parent_node = bst_find.Node.Parent
            if parent_node.NodeKey > key:
                parent_node.LeftChild = None
            else:
                parent_node.RightChild = None
            bst_find.Node.Parent = None
            return bst_find.NodeHasKey
        if bst_find.Node.RightChild is not None:
            ReplacingNode = self.FinMinMax(bst_find.Node.RightChild, FindMax=False)
        else:
            ReplacingNode = bst_find.Node.LeftChild
        self.DeleteNodeByKey(ReplacingNode.NodeKey)
        self._replace_node(bst_find.Node, ReplacingNode)
        return bst_find.NodeHasKey 

    def Count(self):
        if self.Root is None:
            return 0
        return self._number_nodes_in_tree(self.Root)

    # 2.* (бонус +500) Добавьте метод, который находит все пути от корня к листьям, длина которых равна заданной величине.
    def find_all_root_to_leaf_ways(self, n: int):
        if self.Root is None:
            return []
        return self._find_ways(self.Root, 0, n, [])

    def _find_ways(self, Node: BSTNode, current_level: int, n: int, path: list):
        result = []
        if (Node.LeftChild is None) and (Node.RightChild is None) and (current_level == n):
            result.append(path + [Node])
            return result
        if (Node.LeftChild is not None) and (current_level < n):
            result.extend(
                self._find_ways(Node.LeftChild, current_level+1, n, path + [Node])
            )
        if (Node.RightChild is not None) and (current_level < n):
            result.extend(
                self._find_ways(Node.RightChild, current_level+1, n, path + [Node])
            )
        return result
    

