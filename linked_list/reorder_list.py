# leetcode challenge 143: reorder list
# given a linked list L0 -> L1 -> ... Ln-1 -> Ln
# reorder it into L0 -> Ln -> L1 -> Ln-1 ...

# input:  1 -> 2 -> 3 -> 4
# output: 1 -> 4 -> 2 -> 3

# input:  1 -> 2 -> 3 -> 4 -> 5
# output: 1 -> 5 -> 2 -> 4 -> 3


class Node:
    def __init__(self, val=None, next_=None):
        self.val = val
        self.next = next_


def print_list(head):
    while head:
        if head.next:
            print(head.val, "->", end=" ")
        else:
            print(head.val)
        head = head.next


def to_array(head):
    array = []
    while head:
        array.append(head.val)
        head = head.next
    return array


def reorder_list(head):
    """
    Reorder a linked list according to the challenge description.

    Time complexity: O(n) we iterate twice throught the list, sequentially
    Space complexity: O(1) we reorder the list in place

    :param Node head: first node of the linked list
    """
    if not head or not head.next:
        return

    # we find the middle point of the list
    lag = head
    lead = head
    while lead.next and lead.next.next:
        lag = lag.next
        lead = lead.next.next

    # we reverse the linked list after the middle
    reverse = None
    current = lag.next
    while current:
        next_ = current.next
        current.next = reverse
        reverse = current
        current = next_
    lag.next = reverse

    # reorder the list nodes like a zig-zag
    cur = head
    rev = lag.next
    while cur != lag:
        lag.next = rev.next
        rev.next = cur.next
        cur.next = rev
        cur = rev.next
        rev = lag.next


def test1():
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    reorder_list(head)
    assert to_array(head) == [1, 5, 2, 4, 3]
    print("test 1 successful")


def test2():
    head = None
    reorder_list(head)
    assert to_array(head) == []
    print("test 2 successful")


def test3():
    head = Node(1, Node(2, Node(3, Node(4))))
    reorder_list(head)
    assert to_array(head) == [1, 4, 2, 3]
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
