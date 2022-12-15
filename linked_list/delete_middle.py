"""
leetcode 2095: delete the middle node of a linked list

You are given the head of a linked list. Delete the middle node, and return the
head of the modified linked list.

The middle node of a linked list of size n is the floor(n // 2)th node from the
start using 0-based indexing, where floor(x) denotes the largest integer less
than or equal to x.

For n = 1, 2, 3, 4 and 5, the middle nodes are 0, 1, 1, 2 and 2, respectively.
"""


class Node:
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


def delete_middle(head):
    p0 = None
    p1 = p2 = head
    while p2 and p2.next:
        p0 = p1
        p1 = p1.next
        p2 = p2.next.next
    if p0:
        p0.next = p0.next.next
        return head


def test1():
    head = Node(1, Node(3, Node(4, Node(7, Node(1, Node(2, Node(6)))))))
    head = delete_middle(head)
    assert head.next.next.next.val == 1
    print("test 1 successful")


def test2():
    head = Node(1, Node(2, Node(3, Node(4))))
    head = delete_middle(head)
    assert head.next.next.val == 4
    print("test 2 successful")


def test3():
    head = Node(2, Node(1))
    head = delete_middle(head)
    assert head.next is None
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
