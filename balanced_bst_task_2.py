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

    def _is_balanced_subtree(self, Node: BSTNode, current_level: int):
        if Node is None:
            return current_level
        left_max_level = self._is_balanced_subtree(Node.LeftChild, current_level+1)
        right_max_level = self._is_balanced_subtree(Node.RightChild, current_level+1)
        if abs(left_max_level - right_max_level) > 1: 
            return False
        return max(left_max_level, right_max_level)

    def GenerateTree(self, a: list):
        if len(a) == 0:
            self.Root = None
        a = sorted(a)
        self._get_balanced_bst(None, a, 0)

    def IsBalanced(self, root_node: BSTNode):
        if root_node is None:
            return True
        if self._is_balanced_subtree(root_node, 0):
            return True
        return False

    # 2.* Добавьте метод проверки, действительно ли дерево получилось правильным: 
    # для каждого узла ключ левого потомка должен быть меньше его ключа, а ключ правого потомка должен быть больше или равен ключу родителя.
    def IsCorrectBST(self, root_node: BSTNode):
        if root_node is None:
            return True
        return self._is_correct_bst(root_node)

    def _is_correct_bst(self, Node: BSTNode):
        if Node is None:
            return True
        if (Node.LeftChild is not None) and (Node.NodeKey <= Node.LeftChild.NodeKey):
            return False
        if (Node.RightChild is not None) and (Node.NodeKey > Node.RightChild.NodeKey):
            return False
        left_part = self._is_correct_bst(Node.LeftChild)
        right_part = self._is_correct_bst(Node.RightChild)
        return all([left_part, right_part])


