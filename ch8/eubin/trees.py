
from abc import ABC


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

    def _height1(self) -> int:
        """
        runs in O(N**2)
        :param p:
        :return:
        """
        # O(n): for p in self.positions() if p.is_leaf() -> list[Position] (returns an iterable)
        # O(n): max([list comprehension)]) -> loop through the iterable
        # O(n) * O(n) = O(n**2)
        return max([self.depth(p) for p in self.positions() if self.is_leaf(p)])

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

    def positions(self) -> iter:
        pass

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

    def children(self, p: Tree.Position):

        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


class ArrayBinaryTree(BinaryTree):
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
                     element,
                     parent=None,
                     left=None,
                     right=None):
            self.element = element
            self.parent = parent
            self.left = left
            self.right = right

    class Position(BinaryTree.Position):

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

    def _validate(self, p: Position) -> Node:
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

    def root(self) -> Position:
        pass

    def parent(self, p: Position) -> Position:
        pass

    def num_children(self, p: Position) -> int:
        pass

    def children(self, p: Position):
        pass

    def left(self, p: Position) -> Position:
        pass

    def right(self, p: Position) -> Position:
        pass

    def __len__(self) -> int:
        pass
