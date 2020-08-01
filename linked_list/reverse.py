class Node:
    def __init__(self, val=None, next_=None):
        self.val = val
        self.next = next_

    def __str__(self):
        return str(self.val)


def reverse(head):
    rev = None
    while head:
        next_node = head.next
        head.next = rev
        rev = head
        head = next_node
    return rev


def reverse2(head, m, n):
    """
    Leetcode problem 92: reverse linked list from position m to n.
    1 <= m <= n < length of list

    Time complexity: O(n)
    Space complexity: O(1)

    :param Node head: first node of the linked list
    :param int m: index of first node of reversion (starting from 0)
    :param int n: index of last node of reversion (starting from 0)
    :returns: first node of the resulting linked list
    """
    dummy = Node(next_=head)
    current = dummy

    # move to the node just before reversion
    for _ in range(m-1):
        current = current.next

    # find the node immediately following the end of the reversion
    rev = current.next
    for _ in range(n-m+1):
        rev = rev.next

    # do the reversion per se
    head = current.next
    for _ in range(n-m+1):
        tmp = head.next
        head.next = rev
        rev = head
        head = tmp

    # attach the reversed part to the beginning of the list
    current.next = rev

    return dummy.next


def print_list(head):
    while head:
        print(head.val, end="->")
        head = head.next
    print("None")


def print_list_recur(head):
    if head.next:
        print(f"{head.val} -> ", end="")
        return print_list(head.next)
    print(head.val)


def list_to_array(head):
    """
    Convert a linked list into an array.

    :param Node head: first node of linked list
    :returns: list - resulting array
    """
    array = []
    while head:
        array.append(head.val)
        head = head.next
    return array


def test1():
    linked_list = Node(1, Node(2, Node(3)))
    rev = reverse(linked_list)
    assert list_to_array(rev) == [3, 2, 1]
    print("test 1 successful")


def test2():
    L = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    rev = reverse2(L, 2, 4)
    assert list_to_array(rev) == [1, 4, 3, 2, 5]
    print("test 2 successful")


if __name__ == "__main__":
    test1()
    test2()
