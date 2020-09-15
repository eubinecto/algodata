

# python uses duck typing.
# so you should not bound the type of the item that goes to the stack.
# as long as an object behaves like you want, then it is an object that you want
# https://stackoverflow.com/questions/32684720/how-do-i-ensure-parameter-is-correct-type-in-python
class Stack:
    """
    A stack is a LIFO data structure
    """
    def __init__(self) -> None:
        super().__init__()
        # init a list
        self.stack: list = list()

    def pop(self):
        if self.is_empty():
            # if stack is empty, return None
            return None
        return self.stack.pop()

    def push(self, item):
        """
        FIFO. so should put at the beginning of the stack
        :param item:
        :return:
        """
        self.stack.insert(0, item)

    def peek(self):
        if self.is_empty():
            return None
        # just return the first one
        return self.stack[0]

    def is_empty(self):
        return len(self.stack) == 0


class Queue:
    pass

