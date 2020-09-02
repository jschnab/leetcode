# from "cracking the coding interview"
# implement a data structure composed of several
# stacks with a fixed capacity
# when one stack reaches full capacity, items are pushed
# to the next stack
# pop should behave exactly the same way as if there was
# a single stack


class SetStacks:
    def __init__(self, max_height=10):
        self.stacks = [[]]
        self.stack_index = 0
        self.max_height = max_height
        self.total_height = 0

    def push(self, item):
        """
        Push an item to the stack.

        :param item: item to push to the stack
        """
        self.total_height += 1
        if len(self.stacks[self.stack_index]) < self.max_height:
            self.stacks[self.stack_index].append(item)
        else:
            self.stacks.append([item])
            self.stack_index += 1

    def pop(self, index=None):
        """
        Pop an item from the stack.

        :param int index: substack to pop from
        """
        if index is None:
            index = self.stack_index
        if self.isempty:
            raise RuntimeError("pop from empty stack")
        item = self.stacks[index].pop()
        self.total_height -= 1
        while len(self.stacks[self.stack_index]) == 0 and self.stack_index > 0:
            del self.stacks[self.stack_index]
            self.stack_index -= 1
        return item

    @property
    def isempty(self):
        return self.total_height == 0
