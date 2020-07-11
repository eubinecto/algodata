
from abc import ABC
from typing import Generator


class Tree:
    class Position:
        def element(self):
            raise NotImplementedError("this must be implemented by subclasses")

        def __eq__(self, other):
            raise NotImplementedError("this must be implemented by subclasses")

        def __ne__(self, other):
            return not (self == other)

    def root(self) -> Position:
        """
        :return: the position of the root element
        """
        raise NotImplementedError("this must be implemented by subclasses")

    def parent(self, p: Position) -> Position:
        """
        The logic for checking the existance of p in this Tree is to be
        implemented by subclasses, depending on the how the Position abstract
        class is defined.
        :param p: a posiiton
        :return: the position of the parent element
        """
        raise NotImplementedError("this must be implemented by subclasses")

    def num_children(self, p: Position) -> int:
        raise NotImplementedError("this must be implemented by subclasses")

    def children(self, p: Position) -> any:
        raise NotImplementedError("this must be implemented by subclasses")

    def __len__(self) -> int:
        raise NotImplementedError("this must be implemented by subclasses")

    def is_root(self, p: Position) -> bool:
        """
        :param p: a position object
        :return: True of p is a root of the tree, False if not
        """
        return self.root() == p

    def is_empty(self) -> bool:
        """
        :return: True if the size of the tree is zero, False if not
        """
        return len(self) == 0

    def is_leaf(self, p: Position) -> bool:
        """
        :param p: a position object.
        :return: True if the position is leaf, False if not.
        """
        return self.num_children(p) == 0

    def height(self, p=None) -> int:
        if p is None:
            # if p is None, then return the height of the tree
            # which is the height of the root pos.
            p = self.root()

        # return the height of the position
        return self._height2(p)

    # def _height1(self) -> int:
    #     """
    #     runs in O(N**2)
    #     :param p:
    #     :return:
    #     """
    #     # O(n): for p in self.positions() if p.is_leaf() -> list[Position] (returns an iterable)
    #     # O(n): max([list comprehension)]) -> loop through the iterable
    #     # O(n) * O(n) = O(n**2)
    #     return max([self.depth(p) for p in self.positions() if self.is_leaf(p)])
    # def positions(self) -> iter:
    #     pass

    def _height2(self, p: Position) -> int:
        """
        runs in O(N) (recursive)
        :param p:
        :return:
        """
        # base case
        if self.is_leaf(p):
            # the height of a leaf is zero. (def)
            return 0
        else:  # step case
            return 1 + max([self._height2(child) for child in self.children(p)])

    def depth(self, p) -> int:
        if self.is_root(p):
            return 0
        else:
            # 엄마가 두명은 아니잖아? 그냥 줄타고 올라가면 돼.
            # 아이들은 여려명일 수 있으니 height는 제일 키큰놈을 찾아야한다 (max)
            # 1을 더해야 하나 말아야 하나가 고민될 때는, base case를 생각을 한다.
            return 1 + self.depth(self.parent(p))


class LinkedTree(Tree):
    class Position(Tree.Position):

        def element(self):
            pass

        def __eq__(self, other):
            pass

    def root(self) -> Position:
        pass

    def parent(self, p: Position) -> Position:
        pass

    def num_children(self, p: Position) -> int:
        pass

    def children(self, p: Position):
        pass

    def __len__(self) -> int:
        pass


class BinaryTree(Tree, ABC):

    def left(self, p: Tree.Position) -> Tree.Position:
        """
        returns the left pos of the given pos
        :param p:
        :return:
        """
        raise NotImplementedError

    def right(self, p: Tree.Position) -> Tree.Position:
        """
        returns the right pos of the given pos
        :param p:
        :return:
        """
        raise NotImplementedError

    def sibling(self, p: Tree.Position):
        parent = self.parent(p)

        if parent is None:
            return None

        if self.left(parent) == p:
            return self.right(parent)
        else:
            return self.left(parent)

    def children(self, p: Tree.Position) -> Generator:
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


class ArrayBinaryTree(BinaryTree):
    def left(self, p: Tree.Position) -> Tree.Position:
        pass

    def right(self, p: Tree.Position) -> Tree.Position:
        pass

    class Position(BinaryTree.Position):

        def element(self):
            pass

        def __eq__(self, other):
            pass

    def root(self) -> Position:
        pass

    def parent(self, p: Position) -> Position:
        pass

    def num_children(self, p: Position) -> int:
        pass

    def children(self, p: Position):
        pass

    def __len__(self) -> int:
        pass


class LinkedBinaryTree(BinaryTree):
    class Node:
        # saves memory
        __slots__ = 'parent', 'element', "left", "right"

        def __init__(self,
                     element: any,
                     parent=None,
                     left=None,
                     right=None):
            """
            :param element: could be int, str, float, etc
            :param parent: type Node, or None if empty
            :param left: type Node, or None if empty
            :param right: type Node or None if empty
            """
            self.element = element
            self.parent = parent
            self.left = left
            self.right = right

    class Position(BinaryTree.Position):
        """
        사실 Position 이라는 이름은 misleading. "호적"
        """

        def __init__(self,
                     container: BinaryTree,
                     node):
            """
            :param container: any container. could be list, array, .. tree.
            :param node: another Node
            """
            self.container = container
            self.node = node

        def element(self):
            return self.node.element

        def __eq__(self, other):
            return type(self) is type(other)\
                    and self.node is other.node

    def _validate(self, p: 'LinkedBinaryTree.Position') -> Node:
        """
        what is this validating for?
        :param p:
        :return:
        """
        # check type
        if not isinstance(p, self.Position):
            raise TypeError("p must be a proper Position type")

        # check availability
        # the tree contains p.node.
        # container: make it possible to check the availability in O(1)
        if p.container is not self:
            # 너네집 아니야.
            #  근데 p가 뭐냐고.
            raise ValueError("p does not belong to this tree")

        # check deprecated node
        # 이건 왜?
        # 삭제해야하는 노드는 따로 정의해야함. node = None으로 해버리먄 Root랑 구분이 X.
        if p.node.parent is p.node:
            raise ValueError("p is no longer valid")

        # if the position is valid, return the node
        return p.node

    def _make_position(self, node: Node):
        """
        when is a node None?
        e.g. parent(self, p) if p is the position of a root node..
        :param node:
        :return: the position of the node
        """
        return self.Position(self, node) if node is not None else None

    __slots__ = '_root', '_size'

    def __init__(self):
        """
        init an empty binary tree.
        """
        self._root: (LinkedBinaryTree.Position, None) = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self) -> ('LinkedBinaryTree.Position', None):
        # linked binary tree의 posiiton implementation을 사옹.
        return self._make_position(self._root)

    def parent(self, p: 'LinkedBinaryTree.Position') -> ('LinkedBinaryTree.Position', None):
        node = self._validate(p)
        return self._make_position(node.parent)

    def left(self, p: 'LinkedBinaryTree.Position') -> ('LinkedBinaryTree.Position', None):
        node = self._validate(p)
        return self._make_position(node.left)

    def right(self, p: 'LinkedBinaryTree.Position') -> ('LinkedBinaryTree.Position', None):
        node = self._validate(p)
        return self._make_position(node.right)

    def num_children(self, p: 'LinkedBinaryTree.Position') -> int:
        node = self._validate(p)
        count = 0
        if node.left is not None:
            count += 1
        if node.right is not None:
            count += 1
        return count

    def _add_root(self, e: any) -> 'LinkedBinaryTree.Position':
        if self._root is not None:
            raise ValueError("Root already exists")

        self._root = self.Node(e)

        # 이미 root 가 있다면, 애초에 위에서 에러.
        # 때문에 여기까지 왔다면 사이즈는 반드시 1.
        self.size = 1

        return self._make_position(self._root)

    def _add_left(self, p: 'LinkedBinaryTree.Position', e: any) -> 'LinkedBinaryTree.Position':

        node = self._validate(p)

        if node.left is None:
            raise ValueError("left node already exists")

        # 팔다리르 만들어주긴 해야함.
        node.left = self.Node(e)

        # increment size
        self._size += 1

        # 출생신고를 해줘야 해.
        return self._make_position(node.left)

    def _add_right(self, p: 'LinkedBinaryTree.Position', e: any) -> 'LinkedBinaryTree.Position':

        # validate the position
        node = self._validate(p)

        if node.right is not None:
            raise ValueError("the right node already exists")

        node.right = self.Node(e)

        # increment size
        self._size += 1

        return self._make_position(node.right)

    def _replace(self, p: 'LinkedBinaryTree.Position', e: any) -> any:
        """
        replace the elem stored at p with e.
        :param p:
        :param e:
        :return: the "old" element
        """
        # 너 우리집 아이 맞아?
        node = self._validate(p)

        old = node.element

        node.element = e

        return old

    def _delete(self, p) -> any:

        node = self._validate(p)

        # 할머니가 애들 셋을 데리고 있을 수 없으니..
        num_children = self.num_children(p)

        if num_children == 2:
            raise ValueError("cannot delete a p with 2 children")

        # who is the orphan?
        if node.left is None:
            orphan = node.right
        else:
            orphan = node.left

        # 아이에게 부모를 알려줌
        if orphan is not None:
            orphan.parent = node.parent

        # 부모에게 아이를 알려줌
        if node is self._root:
            self._root = orphan
        else:
            # is it the left child?
            if node is node.parent.left:
                node.parent.left = orphan
            else:
                node.parent.right = orphan

        self._size -= 1

        # now the node is deprecated
        node.parent = node

        # the element of the deleted node
        return node.element

    def _attach(self,
                p: 'LinkedBinaryTree.Position',
                t1: 'LinkedBinaryTree',
                t2: 'LinkedBinaryTree'):
        """
        :param p: the position to which the two trees will be attached
        :param t1: to be attached to p as a left child
        :param t2: to be attached to p as a right child
        :return: None
        """

        # error handling
        # 1. validate the position: does the position exist in this tree?
        node = self._validate(p)

        # 2. position must be a leaf
        if not self.is_leaf(p):
            raise ValueError("The position must be a leaf")

        # 3. they all must be of type linked binary tree
        if not isinstance(t1, LinkedBinaryTree) or not isinstance(t2, LinkedBinaryTree):
            raise TypeError("Both t1 and t2 must be of type LinkedBinaryTree")

        # update the size
        self.size += t1.size + t2.size

        # if t1 is not empty, attach t1 and set t1 to be empty
        if not t1.is_empty():
            # 1. let the child know who the new parent is
            t1._root.node.parent = node
            # 2. let the parent know who the new child is
            node.left = t1._root
            # 3. set t1 to be empty
            # but why set t1 to be empty?
            t1._root = None,
            t1._size = 0
        # if t2 is not empty, attach t2 and set t2 to be empty
        if not t2.is_empty():
            # 1. let the child know who the new parent is
            t2._root.parent = node
            # 2. let the parent know who the new child is
            node.right = t2._root
            # but why set t2 to be empty?
            t2._root = None
            t2._size = 0