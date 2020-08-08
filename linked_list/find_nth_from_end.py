# from the book "cracking the code interview"
# given a linked list, return the kth element starting from the end


class Node:
    def __init__(self, val=None, next_=None):
        self.val = val
        self.next = next_


def kth_from_end(head, k):
    """
    Return the kth element starting from the end of the list.

    :param Node head: head of the list
    :param int k: index of element
    :return Node: kth element from the end
    """
    # if list is empty return None
    if not head:
        return

    first = Node(next_=head)
    lead = first
    lag = first

    for _ in range(k):
        # if k > len(list), then return first node
        if not lead.next:
            return first.next

        lead = lead.next


    while lead:
        lead = lead.next
        lag = lag.next

    return lag


def test1():
    head = Node(1, Node(2, Node(3, Node(4))))
    result = kth_from_end(head, 2)
    assert result.val == 3
    print("test 1 successful")


def test2():
    head = Node(1, Node(2, Node(3, Node(4))))
    result = kth_from_end(head, 5)
    assert result.val == 1
    print("test 2 successful")


def test3():
    head = None
    result = kth_from_end(head, 1)
    assert result is None
    print("test 3 successful")


def test4():
    head = Node(1, Node(2, Node(3, Node(4))))
    result = kth_from_end(head, 4)
    assert result.val == 1
    print("test 4 successful")


def test5():
    head = Node(1, Node(2, Node(3, Node(4))))
    result = kth_from_end(head, 1)
    assert result.val == 4
    print("test 5 successful")


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
