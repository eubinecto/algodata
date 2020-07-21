class Node:
    def __init__(self, val):
        self.value = val

    def __eq__(self, other: 'Node'):
        return self.value == other.value


# [element, left_tree, right_tree]
class BinarySearchTree:
    def __init__(self,
                 branch: [Node, None]):
        self.branch = branch
        self.left_tree = None
        self.right_tree = None

    def insert(self, element_node: Node) -> 'BinarySearchTree':
        # 빈 공간에 넣을 때
        if self.branch is None:
            self.branch = element_node

        else:
            # 추가하는 값이 크거나 같은 경우 -> 오른쪽에 붙임
            if element_node.value >= self.branch.value:
                if self.right_tree:
                    self.right_tree.insert(element_node)
                else:
                    self.right_tree = BinarySearchTree(element_node)
            # 추가하는 값이 작은 경우 -> 왼쪽에 붙임
            else:
                if self.left_tree:
                    self.left_tree.insert(element_node)
                else:
                    self.left_tree = BinarySearchTree(element_node)

        return self

    def __eq__(self, other: 'BinarySearchTree'):
        # base case
        if self is None and other is None:
            return True
        elif self is None or other is None:
            return False

        # base case
        return (self.branch == other.branch) and \
               (self.left_tree == other.left_tree) and \
               (self.right_tree == other.right_tree)


class Solution:

    @classmethod
    def ideal_insertion(cls,
                        tree: BinarySearchTree,
                        sorted_ary: list) -> BinarySearchTree:
        size = len(sorted_ary)

        # base case for recursion
        if size == 0:
            return None

        elif size == 1:
            return tree.insert(Node(sorted_ary[0]))

        # get mid index
        center_idx = size // 2

        # inserting mid to tree
        tree.insert(Node(sorted_ary[center_idx]))

        # recursive call
        cls.ideal_insertion(tree, sorted_ary[:center_idx])
        cls.ideal_insertion(tree, sorted_ary[center_idx + 1:])

        return tree

    @classmethod
    def effective_insertion(cls,
                            sorted_ary: list):
        size = len(sorted_ary)

        # base case for recursion
        if size == 0:
            return BinarySearchTree(None)

        elif size == 1:
            return BinarySearchTree(branch=Node(sorted_ary[0]))

        # get mid index
        center_idx = size // 2

        # inserting mid to tree
        tree = BinarySearchTree(branch=Node(sorted_ary[center_idx]))

        # recursive call
        tree.left_tree = cls.effective_insertion(sorted_ary[:center_idx])
        tree.right_tree = cls.effective_insertion(sorted_ary[center_idx + 1:])

        return tree

