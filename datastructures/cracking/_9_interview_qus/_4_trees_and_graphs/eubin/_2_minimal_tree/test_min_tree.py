from unittest import TestCase
from .min_tree import BinarySearchTree, Node, Solution


class TestBinarySearchTree(TestCase):
    def test_insert(self):
        # start with 1
        bstree = BinarySearchTree(root=Node(elem=1))

        # insert -1 to the bstree
        bstree.insert(Node(elem=-2))

        # insert -2 to the bstree
        bstree.insert(Node(elem=-1))

        self.assertEqual(None, bstree.right)
        self.assertEqual(-2, bstree.left.root.elem)
        self.assertEqual(-1, bstree.left.right.root.elem)


class TestSolution(TestCase):
    CASES = [
        # edge case
        (
            [],
            None # convention
         ),
        (
            [1],
            BinarySearchTree(Node(1))
        ),
        (
            [1, 2, 3, 4],
            BinarySearchTree(
                Node(3)).insert(
                Node(2)).insert(
                Node(4)).insert(
                Node(1))
        ),
        (
            [1, 2, 3, 4, 5, 6, 7],
            BinarySearchTree(
                Node(4)).insert(
                Node(2)).insert(
                Node(6)).insert(
                Node(1)).insert(
                Node(3)).insert(
                Node(5)).insert(
                Node(7))
        ),
        (
            [1, 3, 5, 7, 9],
            BinarySearchTree(
                Node(5)).insert(
                Node(3)).insert(
                Node(9)).insert(
                Node(1)).insert(
                Node(7)),
        ),
        (
            [-3, -2, -1],
            BinarySearchTree(
                Node(-2)).insert(
                Node(-3)).insert(
                Node(-1))
        )
    ]

    def test_create_minimal(self):
        for test_in, test_out in self.CASES:
            real = Solution.create_minimal(test_in)
            self.assertEqual(test_out, real)
