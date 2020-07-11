from unittest import TestCase
from unittest.mock import Mock, MagicMock

from ch8.john.trees import LinkedBinaryTree, ArrayBinaryTree


# asert~~~~~( EXPECTED, ACTUAL)

class TestLinkedBinaryTree(TestCase):
    def test__validate(self):
        self.assertEqual(1 + 1, 2)
        # self.fail()

    def test__make_position(self):
        self.fail()

    def test_root(self):
        self.fail()

    def test_parent(self):
        self.fail()

    def test_left(self):
        self.fail()

    def test_right(self):
        self.fail()

    def test_num_children(self):
        self.fail()

    def test__add_root(self):
        self.fail()

    def test__add_left(self):
        self.fail()

    def test__add_right(self):
        self.fail()

    def test__replace(self):
        self.fail()

    def test__delete(self):
        # two children
        t1 = LinkedBinaryTree()
        p1_node = LinkedBinaryTree.Node(None)
        p1 = LinkedBinaryTree.Position(container=t1,
                                       node=p1_node)

        t1._validate = MagicMock(return_value=True)
        t1.num_children = MagicMock(return_value=2)

        with self.assertRaises(ValueError):
            t1._delete(p1)

        # deleting root
        t2 = LinkedBinaryTree()
        p2 = t2._add_root(e=1)

        t2._validate = MagicMock(return_value=p2.node)
        t2.num_children = MagicMock(return_value=1)

        t2_pop_element = t2._delete(p2)
        self.assertEqual(0, len(t2), 'Size of tree (root delete)')
        self.assertEqual(1, t2_pop_element, 'Wrong pop from _delete function')

        # deleting internal node
        def position_for_magicmock(pos):
            if pos == p_root3:
                return p_root3.node
            elif pos == p_left3_1:
                return p_left3_1.node

        t3 = LinkedBinaryTree()
        t3._validate = MagicMock(side_effect=position_for_magicmock)

        p_root3 = t3._add_root(e=1)
        p_left3_1 = t3._add_left(p_root3, e=2)
        p_left3_2 = t3._add_left(p_left3_1, e=3)

        t3_pop_element = t3._delete(p_left3_1)

        self.assertEqual(2, len(t3), 'Size of tree (internal delete)')
        self.assertEqual(p_left3_2.node, p_root3.node.left, 'parent connects to child')
        self.assertEqual(2, t3_pop_element, 'poped element check')

        # deleting leaf node
        def position_for_magicmock_t4(pos):
            if pos == p_root4:
                return p_root4.node
            elif pos == p_left4:
                return p_left4.node
            elif pos == p_right4:
                return p_right4.node

        t4 = LinkedBinaryTree()
        t4._validate = MagicMock(side_effect=position_for_magicmock_t4)

        p_root4 = t4._add_root(e=1)
        p_left4 = t4._add_left(p_root4, e=2)
        p_right4 = t4._add_right(p_root4, e=3)

        t4_pop_left = t4._delete(p_left4)
        self.assertEqual(2, len(t4), 'Size of tree (leaf mid)')
        self.assertEqual(2, t4_pop_left, 'left element check')
        self.assertEqual(None, p_root4.node.left, 'left deleted check')

        t4_pop_right = t4._delete(p_right4)
        self.assertEqual(1, len(t4), 'Size of tree (leaf end)')
        self.assertEqual(3, t4_pop_right, 'right element check')
        self.assertEqual(None, p_root4.node.right, 'right deleted check')

    def test__attach_is_leaf(self):
        t1 = LinkedBinaryTree()
        t2 = LinkedBinaryTree()
        t2._add_root(e=None)
        t2_root = t2.root()
        t3 = LinkedBinaryTree()
        t3._add_root(e=None)
        t3_root = t3.root()

        p_node = LinkedBinaryTree.Node(None)
        p = LinkedBinaryTree.Position(container=t1,
                                      node=p_node)

        t1.is_leaf = MagicMock(return_value=False)
        with self.assertRaises(ValueError):
            t1._attach(p, t2, t3)

    def test__attach_type_check(self):
        t1 = LinkedBinaryTree()
        t2 = LinkedBinaryTree()
        t2._add_root(e=None)
        t2_root = t2.root()
        t3 = ArrayBinaryTree()

        p_node = LinkedBinaryTree.Node(None)
        p = LinkedBinaryTree.Position(container=t1,
                                      node=p_node)

        t1.is_leaf = MagicMock(return_value=True)
        with self.assertRaises(TypeError):
            t1._attach(p, t2, t3)

    def test__attach_general(self):
        # test environment mocking
        t1 = LinkedBinaryTree()
        t2 = LinkedBinaryTree()
        t2._add_root(e=None)
        t2_root = t2.root()
        t3 = LinkedBinaryTree()
        t3._add_root(e=None)
        t3_root = t3.root()

        p_node = LinkedBinaryTree.Node(None)
        p = LinkedBinaryTree.Position(container=t1,
                                      node=p_node)

        # test environment setting
        t1._validate = MagicMock()
        t1._validate.return_value = p_node

        t1.is_leaf = MagicMock()
        t1.is_leaf.return_value = True

        t2._size = 10
        t3._size = 20
        t1._size = 30

        t2.is_empty = MagicMock()
        t2.is_empty.return_value = False

        t3.is_empty = MagicMock()
        t3.is_empty.return_value = False

        # method to be tested
        t1._attach(p, t2, t3)

        left_child = t1.left(p)
        right_child = t1.right(p)

        # testing
        self.assertEqual(60, len(t1), 'Wrong size addition')

        self.assertEqual(left_child, t2_root, 'Wrong left child')
        self.assertEqual(right_child, t3_root, 'Wrong right child')

        self.assertEqual(None, t2._root, 't2 not demolished (root)')
        self.assertEqual(0, t2._size, 't2 not demolished (size)')
        # self.assertEqual(t2.root().node, t2._root)
        self.assertEqual(None, t3._root, 't3 not demolished (root)')
        self.assertEqual(0, t3._size, 't3 not demolished (size)')
