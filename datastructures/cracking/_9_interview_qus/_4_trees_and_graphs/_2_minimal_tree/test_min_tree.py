from unittest import TestCase
from unittest.mock import MagicMock

from .min_tree import BinarySearchTree, Node, Solution


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


class TestSolution(TestCase):
    INs = [
        [],
        [1],
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5, 6, 7],
        [1, 3, 5, 7, 9],
        [-3],
        [-3, -2, -1],

    ]

    OUTs = [
        BinarySearchTree(branch=None),
        BinarySearchTree(
            branch=Node(1)),
        BinarySearchTree(
            branch=Node(3)).insert(
            Node(4)).insert(
            Node(2)).insert(
            Node(1)),
        BinarySearchTree(
            branch=Node(4)).insert(
            Node(2)).insert(
            Node(6)).insert(
            Node(1)).insert(
            Node(3)).insert(
            Node(5)).insert(
            Node(7)),
        BinarySearchTree(
            branch=Node(5)).insert(
            Node(3)).insert(
            Node(9)).insert(
            Node(1)).insert(
            Node(7)),
        BinarySearchTree(
            branch=Node(-3)),
        BinarySearchTree(
            branch=Node(-2)).insert(
            Node(-3)).insert(
            Node(-1))

    ]

    def test_ideal_insertion(self):
        OUT: BinarySearchTree
        for IN, OUT in zip(self.INs, self.OUTs):
            real = Solution.ideal_insertion(
                                 BinarySearchTree(None),
                                 IN)
            self.assertEqual(OUT, real)

    def test_effective_insertion(self):
        OUT: BinarySearchTree
        for IN, OUT in zip(self.INs, self.OUTs):
            real = Solution.effective_insertion(IN)
            self.assertEqual(OUT, real)

