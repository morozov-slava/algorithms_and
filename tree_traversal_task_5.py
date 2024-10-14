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

    # Task 1
    def _wide_node(self, one_level_nodes: list, all_prev_nodes: list):
        if len(one_level_nodes) == 0:
            return all_prev_nodes
        next_level_nodes = []
        for Node in one_level_nodes:
            all_prev_nodes.append(Node)
            if Node.LeftChild is not None:
                next_level_nodes.append(Node.LeftChild)
            if Node.RightChild is not None:
                next_level_nodes.append(Node.RightChild)
        return self._wide_node(next_level_nodes, all_prev_nodes)
    
    def WideAllNodes(self):
        if self.Root is None:
            return []
        return self._wide_node([self.Root], [])

    # Task 2
    def _in_order_deep_search(self, Node):
        all_nodes = []
        if Node.LeftChild is not None:
            all_nodes.extend(self._in_order_deep_search(Node.LeftChild))
        if Node is not None:
            all_nodes.append(Node)
        if Node.RightChild is not None:
            all_nodes.extend(self._in_order_deep_search(Node.RightChild))
        return all_nodes
    
    def _post_order_deep_search(self, Node):
        all_nodes = []
        if Node.LeftChild is not None:
            all_nodes.extend(self._post_order_deep_search(Node.LeftChild))
        if Node.RightChild is not None:
            all_nodes.extend(self._post_order_deep_search(Node.RightChild))
        if Node is not None:
            all_nodes.append(Node)
        return all_nodes
    
    def _pre_order_deep_search(self, Node):
        all_nodes = []
        if Node is not None:
            all_nodes.append(Node)
        if Node.LeftChild is not None:
            all_nodes.extend(self._pre_order_deep_search(Node.LeftChild))
        if Node.RightChild is not None:
            all_nodes.extend(self._pre_order_deep_search(Node.RightChild))
        return all_nodes
    
    def DeepAllNodes(self, approach: int):
        if approach == 0:
            return self._in_order_deep_search(self.Root)
        elif approach == 1:
            return self._post_order_deep_search(self.Root)
        elif approach == 2:
            return self._pre_order_deep_search(self.Root)
        else:
            raise KeyError(f"Unknown approach '{approach}'")

    # 4.* (бонус +500) Добавьте метод, который находит уровень в текущем дереве, сумма значений узлов на котором максимальна.
    # Подумайте, как оптимизировать решение, чтобы производительность была достаточной даже для больших деревьев.
    def find_max_sum_values_tree_level(self):
        if self.Root is None:
            return None
        return self._find_level_with_max_sum_values([self.Root], 0, 0, 0)
    
    def _find_level_with_max_sum_values(self, one_level_nodes: list, current_level: int, max_level: int, max_sum: int):
        if len(one_level_nodes) == 0:
            return max_level
        next_level_nodes = []
        current_sum = 0
        for Node in one_level_nodes:
            if Node.LeftChild is not None:
                next_level_nodes.append(Node.LeftChild)
            if Node.RightChild is not None:
                next_level_nodes.append(Node.RightChild)
            current_sum += Node.NodeKey
        if current_sum > max_sum:
            max_sum = current_sum
            max_level = current_level
        return self._find_level_with_max_sum_values(next_level_nodes, current_level+1, max_level, max_sum)


# 5.* (бонус +500) Учитывая результаты обхода дерева в префиксном и инфиксном порядке, разработайте функцию для восстановления оригинального дерева. 
# Например, префиксный массив: [1,2,4,5,3,6,7] инфиксный массив: [4,2,5,1,6,3,7]
def restorate_keys(tree: BST, pre_order_keys: list, in_order_keys: list):
    if len(pre_order_keys) == 0 or len(in_order_keys) == 0:
        return None
    tree.AddKeyValue(key=pre_order_keys[0], val=0)
    node_index = in_order_keys.index(pre_order_keys[0])
    left_in_order = in_order_keys[:node_index]
    right_in_order = in_order_keys[node_index+1:]
    left_pre_order = pre_order_keys[1:1 + len(left_in_order)]
    right_pre_order = pre_order_keys[1 + len(left_in_order):]
    restorate_keys(tree, left_pre_order, left_in_order)
    restorate_keys(tree, right_pre_order, right_in_order)
    return None


def restorate_tree(pre_order_keys: list, in_order_keys: list):
    tree = BST(node=None)
    restorate_keys(tree, pre_order_keys, in_order_keys)
    return tree
