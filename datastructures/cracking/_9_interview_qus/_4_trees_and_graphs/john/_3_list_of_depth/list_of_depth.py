
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def level_search(self):
        cur_depth = 0
        result = {}

        parent = []
        children = []
        worker = [self.root]
        while True:
            root = worker.pop(0)     # queue contains data on the same level

            if root is not None:        # popped value is None -> the children from the parent is empty
                parent.append(root)     # parent stack is temporarily used
                if root.left:           # append left value
                    children.append(root.left)
                if root.right:          # append right value
                    children.append(root.right)

                if not worker:           # if queue is empty
                    if cur_depth != 0:      # first root -> not needed for the solution
                        # the parents that has been popped from the level
                        # added to dictionary with key as level
                        result[cur_depth] = parent
                    else:
                        pass

                    worker = children    # now children become worker
                    children = []       # empty the children for new children
                    cur_depth += 1      # increase the depth

            if not worker:
                break

        return result



class Solution:
    @classmethod
    def solution1(cls, tree: BinaryTree):
        cur_depth = 0
        cnt = 0
        result = {

        }







if __name__ == '__main__':
    a = BinaryTree(1)
    a.insert(3)





