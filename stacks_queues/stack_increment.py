# leetcode challenge 1381: design a stack with an 'increment' operation
# design a stack class with an 'increment' method that increments the bottom
# k elements of the stack by val: stack.increment(k, val)
# if there are less than k elements in the stack we increment all elements


class Stack:
    def __init__(self, max_size=100):
        self.items = []
        self.inc = []  # list of increment values
        self.max_size = max_size

    def push(self, x):
        if len(self.items) < self.max_size:
            self.items.append(x)
            self.inc.append(0)

    def pop(self):
        if len(self.items) > 0:
            if len(self.inc) > 1:
                self.inc[-2] += self.inc[-1]
            return self.items.pop() + self.inc.pop()
        return -1

    def increment(self, k, val):
        """
        We do lazy increments, meaning that we will increment
        stored items when they are popped, so we store increments
        in a list.
        """
        if self.inc:
            self.inc[min(k, len(self.items)) - 1] += val
