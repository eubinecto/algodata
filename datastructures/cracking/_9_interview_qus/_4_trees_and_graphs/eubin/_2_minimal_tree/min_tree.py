from typing import List


class Node:
    """
    A node class to be used
    for readability
    """

    def __init__(self, elem: int):
        self.elem = elem

    def __lt__(self, other: 'Node'):
        return self.elem < other.elem

    def __eq__(self, other):
        return self.elem == other.elem


class BinarySearchTree:
    """
    Binary Search Tree.
    the root of the left bstree is less than the root of the parent.
    the root of the right bstree is geq to the root of the parent
    """

    def __init__(self, root: [Node, None]):
        self.root = root
        # left and right are empty trees
        self.left = None
        self.right = None

    def insert(self, node: Node) -> 'BinarySearchTree':
        """
        insert a node to the binary tree.
        if the node is less than the root node, insert it as the left child
        else, insert the node as the right child
        :param node: a node object to insert.
        """
        if self.root is None:  # empty tree
            self.root = node
        else:
            if node < self.root:
                if self.left is None:
                    self.left = BinarySearchTree(root=node)
                else:
                    self.left.insert(node)
            else:
                if self.right is None:
                    self.right = BinarySearchTree(root=node)
                else:
                    self.right.insert(node)

        return self

    # to be used with testing
    def __eq__(self, other: 'BinarySearchTree'):
        # base case
        if self is None and other is None:
            return True
        elif self is None or other is None:
            return False

        # step case
        # separate comparison for break point
        root_eq = self.root == other.root
        left_eq = self.left == other.left
        right_eq = self.right == other.right
        return root_eq and left_eq and right_eq

    def __str__(self):
        return "left:{}, root:{}, right:{}".format(str(self.left.root),
                                                   str(self.root),
                                                   str(self.right.root))


class Solution:
    @classmethod
    def create_minimal(cls, sorted_array: List[int]) -> [BinarySearchTree, None]:
        # find the next "ideal" element
        size = len(sorted_array)
        if size == 0:
            return None
        if size == 1:
            return BinarySearchTree(Node(sorted_array[0]))

        # the idx for the central value
        center_idx = size // 2
        # insert the ideal elem
        bs_tree = BinarySearchTree(Node(elem=sorted_array[center_idx]))
        # recursive call to itself: left
        bs_tree.left = cls.create_minimal(sorted_array=sorted_array[:center_idx])
        # recursive call to itself: right (excluding the central one)
        bs_tree.right = cls.create_minimal(sorted_array=sorted_array[center_idx + 1:])

        return bs_tree
