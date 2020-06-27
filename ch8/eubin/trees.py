
class Tree:
    class Position:
        # 왜 추가 파라미터가 없으면 init 구현필요 X.

        def element(self):
            raise NotImplementedError("this must be implemented by subclasses")

        def __eq__(self, other):
            raise NotImplementedError("this must be implemented by subclasses")

        def __ne__(self, other):
            return not (self == other)

    # to be implemented by
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

    def children(self, p: Position):
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
