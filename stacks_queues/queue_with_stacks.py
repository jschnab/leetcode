# leetcode challenge 225: implement a queue using stacks


class Queue:
    def __init__(self):
        self.instack = []
        self.outstack = []
        self.length = 0

    def push(self, x):
        self.instack.append(x)
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise RuntimeError("Can't pop empty queue")
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        self.length -= 1
        return self.outstack.pop()

    def peek(self):
        if self.length == 0:
            return
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack[-1]

    @property
    def is_empty(self):
        return self.length == 0
