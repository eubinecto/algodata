from abc import ABCMeta, abstractmethod


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
    def positions(self):
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
    def children(self, p: Position):
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
        # self.postions(p) returns iterable of all positions as iterable.
        return 1 + max(self.depth(position) for position in self.positions() if self.is_leaf(position))

    def _height2(self, p:Position) -> int:
        """
        :param p: query position
        :return: integer
        """
        if self.is_leaf(p):
            return 0

        return 1 + max(self._height2(child) for child in self.children(p))

    def height(self, p:Position =None) -> int:
        """
        height is counted from lowest leaf up to the query position
        when counting, itself is excluded.
        :param p: query position
        :return: integer
        """
        if p is None:
            p = self.root()

        return self._height2(p)




class LinkedTree(Tree):
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

    def children(self, p: Position):
        pass

    def __len__(self) -> int:
        pass


class BinaryTree(Tree, metaclass=ABCMeta):
    pass


class ArrayBinaryTree(BinaryTree):
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


class LinkedBinaryTree(BinaryTree):
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
