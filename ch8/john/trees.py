class Tree:
    class Position:
        def element(self):
            raise NotImplementedError("Must be implemented in subclass")

        def __eq__(self, other):
            raise NotImplementedError("Must be implemented in sublcass")

        def __ne__(self, other):
            return not (self == other)

    def root(self) -> Position:
        """

        :return: position of root of tree T.
        """
        raise NotImplementedError("Must be implemented in sublcass")

    def parent(self, p: Position) -> Position:
        """

        :param p: query position
        :return: position of parent of query position
        """
        raise NotImplementedError("Must be implemented in sublcass")

    def num_children(self, p: Position) -> int:
        """

        :param p: query position
        :return: number of children
        """
        raise NotImplementedError("Must be implemented in sublcass")

    def children(self, p: Position):
        """

        :param p: query position
        :return: children of query position
        """
        raise NotImplementedError("Must be implemented in sublcass")

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


class BinaryTree(Tree):
    pass


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
