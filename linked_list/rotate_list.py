# leetcode problem 61: rotate linked lists
# given a linked list, rotate the list towards the right by k places (k >= 0)
# input: 1->2->3->4->5, k = 2
# output: 4->5->1->2->3


class Node:
    def __init__(self, value=None, next_=None):
        self.value = value
        self.next = next_


def len_list(head):
    """
    Return the length of a linked list.

    :param Node head: first node of the linked list
    :return int: number of nodes in the list
    """
    n = 0
    first = Node(None, head)
    current = first
    while current.next:
        n += 1
        current = current.next
    return n


def rotate_right(head):
    """
    Perform a single list rotation.

    :param Node head: first node of the linked list
    :return Node: first node of the linked list
    """
    if not head or not head.next:
        return head

    # find the new list head
    first = Node(None, head)
    current = first
    while current.next.next:
        current = current.next
    newhead = current.next

    # re-organize links
    current.next = None
    newhead.next = head

    return newhead


def rotate_k_places(head, k):
    """
    Rotate a linked list by k places.

    :param Node head: first node of the linked list
    :return Node: first node of the linked list
    """
    # make sure k is < n (otherwise redundant rotations)
    n = len_list(head)
    if n > 0 and k >= n:
        k %= n

    for _ in range(k):
        head = rotate_right(head)

    return head


def make_list(values):
    """
    :param list values: source of values to build the linked list
    :return Node: head of the linked list
    """
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head


def traverse(head):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result


def test1():
    head = make_list([1, 2, 3, 4])
    assert traverse(head) == [1, 2, 3, 4]
    print("test 1 successful")


def test2():
    head = make_list([1, 2, 3, 4, 5])
    assert traverse(rotate_k_places(head, 2)) == [4, 5, 1, 2, 3]
    print("test 2 successful")


def test2():
    head = make_list([1, 2, 3, 4, 5])
    assert traverse(rotate_k_places(head, 2)) == [4, 5, 1, 2, 3]
    print("test 2 successful")


def test3():
    head = make_list([1, 2, 3, 4, 5])
    assert traverse(rotate_k_places(head, 24)) == [2, 3, 4, 5, 1]
    print("test 3 successful")


def test4():
    head = make_list([1])
    assert traverse(rotate_k_places(head, 9)) == [1]
    print("test 4 successful")


def test5():
    head = None
    assert traverse(rotate_k_places(head, 100)) == []
    print("test 5 successful")


def test6():
    head = make_list([1, 2, 3])
    assert traverse(rotate_k_places(head, 6)) == [1, 2, 3]
    print("test 6 successful")



if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
