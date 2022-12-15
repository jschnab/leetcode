"""
leetcode 328: odd even linked list

Given the head of a singly linked list, group all the nodes with odd indices
together followed by the nodes with even indices, and return the reordered
list.

The first node is considered odd, the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain
as it was in the input.

You must solve the problem in O(1) extra space complexity, and O(n) time
complexity.
"""


class Node:
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def odd_even(head):
    if not head:
        return
    cur_odd = head
    head_even = cur_even = head.next
    while cur_even and cur_even.next:
        cur_odd.next = cur_even.next
        cur_odd = cur_odd.next
        cur_even.next = cur_odd.next
        cur_even = cur_even.next
    cur_odd.next = head_even
    return head


def test1():
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    result = odd_even(head)
    assert list_to_array(result) == [1, 3, 5, 2, 4]
    print("test 1 successful")


def test2():
    head = Node(2, Node(1, Node(3, Node(5, Node(6, Node(4, Node(7)))))))
    result = odd_even(head)
    assert list_to_array(result) == [2, 3, 6, 7, 1, 5, 4]
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
