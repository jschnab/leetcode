# leetcode challenge 445: add two numbers II
# given two non-empty linked lists representing two non-negative integers,
# where the most significant digit comes first,
# return a linked list which is the sum of the two numbers

# input: 7 -> 2 -> 4 -> 3 and 5 -> 6 -> 4
# output: 7 -> 8 -> 0 -> 7

# input: 0 and 0
# output: 0


class Node:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def add_two_lists(l1, l2):
    """
    Add two linked lists according to the challenge description.

    Time complexity: O(n) we iterate through all items once
    Space complexity: O(n) we build a new linked list as a result

    :param Node l1: head of first linked list
    :param Node l2: head of second linked list
    :returns: Node - head of resulting linked list
    """
    i1 = 0
    i2 = 0
    while l1:
        i1 = i1 * 10 + l1.val
        l1 = l1.next
    while l2:
        i2 = i2 * 10 + l2.val
        l2 = l2.next

    i3 = i1 + i2
    if i3 == 0:
        return Node()

    # build the resulting linked list
    head = None
    tail = None
    while i3 > 0:
        head = Node(i3 % 10)
        head.next = tail
        tail = head
        i3 //= 10

    return head
