# leetcode challenge 155: min stack
# design a stack that supports push, pop, top, and retrieving
# the minimum element in constant time


class MinStack:
    def __init__(self):
        # items is a list of tuples where the first element one of the
        # pushed values and the second element is the stack minimum when
        # the element was pushed
        self.items = []

    def push(self, x):
        if not self.items:
            mini = x
        else:
            mini = min(self.items[-1][1], x)
        self.items.append((x, mini))

    def pop(self):
        if self.items:
            return self.items.pop()[0]

    def top(self):
        if self.items:
            return self.items[-1][0]

    def get_min(self):
        if self.items:
            return self.items[-1][1]
