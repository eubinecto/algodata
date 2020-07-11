from unittest import TestCase
from unittest.mock import MagicMock, Mock

from ch8.eubin.trees import LinkedBinaryTree, ArrayBinaryTree


class TestLinkedBinaryTree(TestCase):
    def test__attach(self):
        # make mocks: t1 and t2
        t1: LinkedBinaryTree = LinkedBinaryTree()
        t1._add_root(e=None)
        t2: LinkedBinaryTree = LinkedBinaryTree()
        t2._add_root(e=None)
        t3: LinkedBinaryTree = LinkedBinaryTree()
        p: LinkedBinaryTree.Position = LinkedBinaryTree.Position(container=t3,
                                                                 node=LinkedBinaryTree.Node(element=None))
        # set up mocks before test
        # they are not empty
        t1.is_empty = MagicMock()
        t1.is_empty.return_value = False
        t2.is_empty = MagicMock()
        t2.is_empty.return_value = False
        t1._size = 10
        t2._size = 20
        t3._size = 30

        # p should be a leaf
        t3.is_leaf = MagicMock()
        t3.is_leaf.return_value = True

        # get the root node
        # before attach
        t1_root = t1._root
        t2_root = t2._root

        # test
        t3._attach(p, t1, t2)
        left = p.node.left
        right = p.node.right

        # test if they where successfully attached.
        # first = Expected, second = Actual
        self.assertEqual(t1_root, left)
        self.assertEqual(t2_root, right)
        self.assertEqual(60, len(t3))

        # check if t1 and t2 are reset
        self.assertEqual(None, t1._root)
        self.assertEqual(0, len(t1))
        self.assertEqual(None, t2._root)
        self.assertEqual(0, len(t2))

    def test__attach_p_is_not_leaf(self):
        t1 = LinkedBinaryTree()
        t2 = LinkedBinaryTree()
        t3 = LinkedBinaryTree()
        p = LinkedBinaryTree.Position(container=t3,
                                      node=LinkedBinaryTree.Node(element=1))

        t3.is_leaf = MagicMock(return_value=False)

        with self.assertRaises(ValueError):
            t3._attach(p, t1, t2)

    def test__attach_invalid_type(self):
        t1 = ArrayBinaryTree()
        t2 = ArrayBinaryTree()
        t3 = LinkedBinaryTree()
        p = LinkedBinaryTree.Position(container=t3,
                                      node=LinkedBinaryTree.Node(element=1))

        t3.is_leaf = MagicMock(return_value=True)

        with self.assertRaises(TypeError):
            # type collision intended
            t3._attach(p, t1, t2)

    def test__delete_root(self):
        t1 = LinkedBinaryTree()
        # assume that p1 is valid
        # add root with an element
        root_pos = t1._add_root(e=1)
        # this is how you use side effect
        t1._validate = MagicMock(return_value=root_pos.node)
        # the root should be deleted
        del_elem = t1._delete(root_pos)

        self.assertEqual(1, del_elem, "the popped element is invalid")
        self.assertEqual(0, len(t1))

    def test__delete_internal(self):
        t1 = LinkedBinaryTree()
        root_pos = t1._add_root(e=1)
        left1_pos = t1._add_left(root_pos, e=2)
        left2_pos = t1._add_left(left1_pos, e=3)

        # define a side effect for building the mock
        # use side effect for conditional return values
        def side_effect(pos: LinkedBinaryTree.Position) -> LinkedBinaryTree.Node:
            if pos is root_pos:
                return root_pos.node
            elif pos is left1_pos:
                return left1_pos.node
            elif pos is left2_pos:
                return left2_pos.node
        # define a side effect
        t1._validate = MagicMock(side_effect=side_effect)

        # the method to test
        del_elem = t1._delete(left1_pos)

        # test it
        self.assertEqual(left2_pos.node, root_pos.node.left)
        # check the size
        self.assertEqual(2, len(t1))
        # check if the deleted node
        self.assertEqual(left1_pos.node.element, del_elem)

    def test__delete_leaf(self):
        t1 = LinkedBinaryTree()
        root_pos = t1._add_root(e=1)
        left1_pos = t1._add_left(root_pos, e=2)
        right1_pos = t1._add_right(root_pos, e=3)

        # define a side effect for building the mock
        # use side effect for conditional return values
        def side_effect(pos: LinkedBinaryTree.Position) -> LinkedBinaryTree.Node:
            if pos is root_pos:
                return root_pos.node
            elif pos is left1_pos:
                return left1_pos.node
            elif pos is right1_pos:
                return right1_pos.node

        # register a side effect
        t1._validate = MagicMock(side_effect=side_effect)

        # delete the left leaf node
        del_elem1 = t1._delete(left1_pos)
        # test it
        self.assertEqual(None, root_pos.node.left)
        self.assertEqual(2, len(t1))
        self.assertEqual(left1_pos.node.element, del_elem1)
        # delete the right leaf node
        del_elem2 = t1._delete(right1_pos)
        # test it
        self.assertEqual(None, root_pos.node.right)
        self.assertEqual(1, len(t1))
        self.assertEqual(right1_pos.node.element, del_elem2)

    def test_delete_two_children(self):
        t1 = LinkedBinaryTree()
        root_pos = t1._add_root(e=1)
        left1_pos = t1._add_left(root_pos, e=2)
        left2_pos = t1._add_left(left1_pos, e=3)
        right2_pos = t1._add_right(left1_pos, e=4)

        def side_effect(pos: LinkedBinaryTree.Position) -> LinkedBinaryTree.Node:
            if pos is root_pos:
                return root_pos.node
            elif pos is left1_pos:
                return left1_pos.node
            elif pos is left2_pos:
                return left2_pos.node
            elif pos is right2_pos:
                return right2_pos.node

        # check if it raises a ValueError
        with self.assertRaises(ValueError):
            # this method must raise the exception
            t1._delete(left1_pos)












