from abc import ABCMeta, abstractmethod
from typing import Generator, Iterator, TypeVar


class Tree(metaclass=ABCMeta):
    class Position:
        @abstractmethod
        def element(self):
            raise NotImplementedError("Must be implemented in subclass")

        @abstractmethod
        def __eq__(self, other):
            raise NotImplementedError("Must be implemented in sublcass")

        def __ne__(self, other):
            return not (self == other)

    @abstractmethod
    def positions(self) -> Generator[Position, ...]:
        pass

    @abstractmethod
    def root(self) -> Position:
        """
        :return: position of root of tree T.
        """
        raise NotImplementedError("Must be implemented in sublcass")

    @abstractmethod
    def parent(self, p: Position) -> Position:
        """
        :param p: query position
        :return: position of parent of query position
        """
        raise NotImplementedError("Must be implemented in sublcass")

    @abstractmethod
    def num_children(self, p: Position) -> int:
        """
        :param p: query position
        :return: number of children
        """
        raise NotImplementedError("Must be implemented in sublcass")

    @abstractmethod
    def children(self, p: Position) -> Generator[Position, ...]:
        """
        :param p: query position
        :return: children of query position
        """
        raise NotImplementedError("Must be implemented in sublcass")

    @abstractmethod
    def __len__(self) -> int:
        raise NotImplementedError("Must be implemented in sublcass")

    # concrete implementation
    def is_root(self, p: Position) -> bool:
        """
        :param p: query position
        :return: either the position is root or not
        """
        return self.root() == p

    def is_leaf(self, p: Position) -> bool:
        """
        :param p: query position
        :return: either the position is leaf or not
        leaf is defined as the position that does not have children
        """
        return self.num_children(p) == 0

    def is_empty(self) -> bool:
        """
        :return: either the tree is empty or not
        """
        return len(self) == 0

    def depth(self, p: Position) -> int:
        """
        depth is counted from top down
        when counting, itself is excluded.
        :param p: Query position
        :return: integer
        """
        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))

    def _height1(self) -> int:
        """
        :return: integer
        """
        # As this is not recursive solution, base case is not needed.
        # self.positions(p) returns iterable of all positions as iterable.
        return 1 + max(self.depth(position) for position in self.positions() if self.is_leaf(position))

    def _height2(self, p: Position) -> int:
        """
        :param p: query position
        :return: integer
        """
        if self.is_leaf(p):
            return 0

        return 1 + max(self._height2(child) for child in self.children(p))

    def height(self, p: Position = None) -> int:
        """
        height is counted from lowest leaf up to the query position
        when counting, itself is excluded.
        :param p: query position
        :return: integer
        """
        if p is None:
            p = self.root()

        return self._height2(p)


class LinkedTree(Tree, metaclass=ABCMeta):
    class Position(Tree.Position):
        @abstractmethod
        def element(self):
            raise NotImplementedError("Must be implemented in subclass")

        @abstractmethod
        def __eq__(self, other):
            raise NotImplementedError("Must be implemented in sublcass")

        def __ne__(self, other):
            return not (self == other)

    def root(self) -> Position:
        pass

    def parent(self, p: Position) -> Position:
        pass

    def num_children(self, p: Position) -> int:
        pass

    def children(self, p: Position) -> Generator[Position, ...]:
        pass

    def __len__(self) -> int:
        pass


class BinaryTree(Tree, metaclass=ABCMeta):
    @abstractmethod
    def left(self, p: Tree.Position) -> [Tree.Position, None]:
        """
        :param p: Query position
        :return: left child
        """
        return NotImplementedError("must be implemented in subclass")

    @abstractmethod
    def right(self, p: Tree.Position) -> [Tree.Position, None]:
        """
        :param p: Query position
        :return: right child
        """
        return NotImplementedError("must be implemented in subclass")

    @abstractmethod
    def sibling(self, p: Tree.Position) -> [Tree.Position, None]:
        """
        :param p:
        :return:
        """
        parent = self.parent(p)
        if parent is None:  # p is root
            return None

        if self.left(parent) == p:
            return self.right(parent)
        else:
            return self.left(parent)

    def children(self, p: Tree.Position) -> Generator[Tree.Position, Tree.Position]:
        """
        :param p: Query position (parent)
        :return: Generator
        """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


class ArrayBinaryTree(BinaryTree, metaclass=ABCMeta):
    class Position(BinaryTree.Position):
        @abstractmethod
        def element(self):
            raise NotImplementedError("Must be implemented in subclass")

        @abstractmethod
        def __eq__(self, other):
            raise NotImplementedError("Must be implemented in sublcass")

        def __ne__(self, other):
            return not (self == other)

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


class LinkedBinaryTree(BinaryTree, metaclass=ABCMeta):
    class Node:
        __slots__ = 'element', 'parent', 'left', 'right'

        def __init__(self,
                     element: any,
                     parent=None,
                     left=None,
                     right=None):
            """
            :param element: data: any
            :param parent: parent node
            :param left: left child node
            :param right: right child node
            """
            self.element = element
            self.parent = parent
            self.left = left
            self.right = right

    class Position(BinaryTree.Position):  # 호적같은 개념 ㅋㅋㅋㅋㅋㅋㅋ
        def __init__(self, container: BinaryTree, node):
            """
            Constructor should not be invoked by user
            :param container: Any box that contains nodes but the relationship between node is out of interest.
            :param node: node
            """
            self.container = container
            self.node = node

        @abstractmethod
        def element(self):
            return self.node.element

        @abstractmethod
        def __eq__(self, other):
            """
            Python returns false even when the type is different
            Because two of them are different not one is wrong.
            (wrong -> type error)
            """
            return type(other) is type(self) and other.node is self.node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p: Position) -> Node:
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        # this logic is implemented with position class
        # when checking that the node is in the tree or not can take O(N) when the tree is list
        # but when position(container, node) then searching that position is in the tree or not takes O(1).
        if p.container is not self:
            raise ValueError('p does not belong to this container')
        # this logic is built because of root node definition
        # root node has None as parent so deleted position must have something different
        # which is making parent as self
        if p.node.parent is p.node:
            raise ValueError('p is no longer valid')
        return p.node

    def _make_position(self, node) -> Position:
        return self.Position(self, node) if node is not None else None  ###????????????

    # --------------------------- Binary Tree Constructor ---------------------------------
    __slots__ = '_root', '_size'

    def __init__(self):
        """
        constructed with empty tree
        """
        self._root: [LinkedBinaryTree.Position, None] = None
        self._size: int = 0

    def __len__(self):
        return self._size

    def root(self) -> [Position, None]:
        return self._make_position(self._root)

    def parent(self, p: Position) -> Position:
        node = self._validate(p)
        return self._make_position(node.parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node.left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node.right)

    def num_children(self, p: Position) -> int:
        node = p.node
        count = 0
        if node.left is not None:
            count += 1
        if node.right is not None:
            count += 1
        return count

    # ------------------------ update Methods -------------------------

    def _add_root(self, e: any) -> Position:
        """

        :param e: element
        :return: position
        """
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self.Node(e)
        return self._make_position(self._root)

    def _add_left(self, p: Position, e: any) -> Position:
        """

        :param p: position that will be parent
        :param e: child data
        :return: position of left child
        """
        node = self._validate(p)
        if node.left is not None:
            raise ValueError('Left exists')
        self._size += 1
        node.left = self.Node(e)

        return self._make_position(node.left)  # 자식 출생신고하기 -> 호적을 붙여줌.

    def _add_right(self, p: Position, e: any) -> Position:
        """

        :param p: position that will be parent
        :param e: child data
        :return: position of right child
        """
        node = self._validate(p)
        if node.left is not None:
            raise ValueError('Right exists')
        self._size += 1
        node.right = self.Node(e)

        return self._make_position(node.right)

    def _replace(self, p: Position, e: any) -> any:
        """

        :param p: position that element will be replaced
        :param e: new element
        :return: old element
        """
        node = self._validate(p)
        old = node.element
        node.element = e
        return old

    def _delete(self, p: Position) -> any:      # expel
        """
        :param p: position that will be eliminated
        :return: element from the node in the position
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p has two children')
        child = node.left if node.left else node.right

        # telling to child that your new parent is my grand parent.
        if child is not None:
            node.parent = child.parent

        # the node that doesn't have parent -> child becomes root
        if node is self._root:
            self._root = child
        else:   # telling my parent to have grand child as new child
            parent = node.parent
            if node is parent.left:
                parent.left = child
            else:
                parent.right = child

        self._size -= 1
        node.parent = node  # noticing that this node is deleted node
        return node.element

    def _attach(self, p: Position, t1: 'LinkedBinaryTree', t2: 'LinkedBinaryTree'):
        pass
