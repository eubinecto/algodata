from unittest import TestCase
from unittest.mock import MagicMock

from .min_tree import BinarySearchTree, Node


class TestBinarySearchTree(TestCase):
    def test_insert(self):
        """
                     3
                 1       5
            -3      2
                -2
        """

        tree = BinarySearchTree(Node(3))

        tree.insert(Node(5))
        tree.insert(Node(1))
        tree.insert(Node(-3))
        tree.insert(Node(-2))
        tree.insert(Node(2))

        self.assertEqual(3, tree.branch.value)
        self.assertEqual(5, tree.right_tree.branch.value)
        self.assertEqual(1, tree.left_tree.branch.value)
        self.assertEqual(-3, tree.left_tree.left_tree.branch.value)
        self.assertEqual(2, tree.left_tree.right_tree.branch.value)
        self.assertEqual(-2, tree.left_tree.left_tree.right_tree.branch.value)


