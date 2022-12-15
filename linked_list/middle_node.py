"""
leetcode 876: middle node of linked list

Given the head of a singly linked list, return th emiddle node of the linked
list.

If there are two middle nodes, return the second middle node.
"""


class Node:
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


def middle(head):
    p1 = p2 = head
    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next
    return p1


def test1():
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    assert middle(head) == head.next.next
    print("test 1 successful")


def test2():
    head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))
    assert middle(head) == head.next.next.next
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
