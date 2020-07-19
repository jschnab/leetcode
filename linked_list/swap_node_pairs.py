# leetcode problem 24: swap nodes in pairs
# given a linked list, swap every two adjacent nodes and return list head
# do not modify the value of the nodes, only nodes should be changed
# input: 1->2->3->4
# output: 2->1->4->3


class Node:
    def __init__(self, value=None, next_=None):
        self.value = value
        self.next = next_


def swap_pairs(head):
    """
    :param Node head: first node of the linked list
    :return Node: first node of the linked list
    """
    first = Node(next_=head)
    current = first
    while current.next and current.next.next:
        A = current.next
        B = A.next
        current.next = B
        tmp = B.next
        B.next = A
        A.next = tmp
        current = current.next.next
    return first.next


def make_list(values):
    """
    :param list values: source of values to build the linked list
    :return Node: head of the linked list
    """
    if not values:
        return Node()
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
    head = make_list([1, 2, 3, 4])
    assert traverse(swap_pairs(head)) == [2, 1, 4, 3]
    print("test 2 successful")


def test3():
    head = make_list([1, 2, 3, 4, 5])
    assert traverse(swap_pairs(head)) == [2, 1, 4, 3, 5]
    print("test 3 successful")


def test4():
    head = None
    assert traverse(swap_pairs(head)) == []
    print("test 4 successful")


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
