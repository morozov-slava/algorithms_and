class BSTNode:
    def __init__(self, key, parent):
        self.NodeKey = key
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None
        self.Level = 0
        
class BalancedBST:
    def __init__(self):
    	self.Root = None

    def _get_balanced_bst(self, parent_node: BSTNode, array: list, current_level: int):
        if len(array) == 0:
            return None  
        mid_i = len(array) // 2
        RootNode = BSTNode(key=array[mid_i], parent=parent_node)
        RootNode.Level = current_level
        if parent_node is None:
            self.Root = RootNode
        RootNode.LeftChild = self._get_balanced_bst(RootNode, array[:mid_i], current_level+1)
        if len(array) > 2:
            RootNode.RightChild = self._get_balanced_bst(RootNode, array[mid_i+1:], current_level+1)
        return RootNode
        
    def GenerateTree(self, a: list):
        if len(a) == 0:
            self.Root = None
        a = sorted(a)
        self._get_balanced_bst(None, a, 0)

    def IsBalanced(self, root_node):
        return False # сбалансировано ли дерево с корнем root_node


