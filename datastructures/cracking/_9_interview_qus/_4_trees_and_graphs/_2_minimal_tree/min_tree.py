
class Node:
    def __init__(self, val):
        self.value = val


# [element, left_tree, right_tree]
class BinarySearchTree:
    def __init__(self,
                 branch: Node,
                 left_tree: 'BinarySearchTree' = None,
                 right_tree: 'BinarySearchTree' = None):
        self.branch = branch
        self.left_tree = left_tree
        self.right_tree = right_tree

    def insert(self, element_node):
        # 추가하는 값이 크거나 같은 경우 -> 오른쪽에 붙임
        if element_node.value >= self.branch.value:
            if self.right_tree:
                self.right_tree.insert(element_node)
            else:
                self.right_tree = BinarySearchTree(element_node)
        # 추가하는 값이 작은 경우 -> 왼쪽에 붙임
        else:
            if self.left_tree:
                self.left_tree.insert(element_node)
            else:
                self.left_tree = BinarySearchTree(element_node)

