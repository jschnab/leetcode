# from the book 'cracking the code interview'
# sort a stack with no other data structure
# than another stack


import random


class Stack:
    def __init__(self, items=None):
        self.items = items or []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if self.items:
            return self.items.pop()

    @property
    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

    @property
    def top(self):
        return self.items[-1]

    def __str__(self):
        return str(self.items)


def sort_stack(stack):
    """
    Sort a stack 'in place'.

    Time complexity: O(n^2) worst case (and average case?)
                     O(n) in best case (stack already sorted)
    Space complexity: O(n) we use another stack to store items

    :param Stack stack: stack to sort
    """
    buf = Stack()
    while not stack.is_empty:
        current = stack.pop()
        while not buf.is_empty and current > buf.top:
            stack.push(buf.pop())
        buf.push(current)
    while buf:
        stack.push(buf.pop())


def test1():
    stack = Stack([random.randint(0, 100) for _ in range(10)])
    print("before sorting:", stack)
    sort_stack(stack)
    print("after sorting:", stack)


def test2():
    stack = Stack([1, 2, 3, 4, 5])
    print("before sorting:", stack)
    sort_stack(stack)
    print("after sorting:", stack)


def test3():
    stack = Stack([5, 4, 3, 2, 1])
    print("before sorting:", stack)
    sort_stack(stack)
    print("after sorting:", stack)


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
