# problem 1474: delete n nodes after m nodes in a linked list
# input: 1 -> 2 -> 3 -> 4 -> 5, n = 1, m = 2
# output: 1 -> 2 -> 4 -> 5


class Node:
    def __init__(self, val=None, next_=None):
        self.val = val
        self.next = next_


def delete_n_after_m(head, m, n):
    """
    :param Node head: first node of the linked list
    :param int m: number of nodes to skip before deleting nodes
    :param int n: number of nodes to delete
    :return Node: first node of the resulting linked list

    Time complexity: O(n)
    Space complexity: O(1)
    """
    dummy = Node(next_=head)
    current = dummy
    while current.next:
        if m == 0:
            lead = current.next
            while n > 0:
                lead = lead.next
                n -= 1
            current.next = lead
        if current.next:
            current = current.next
            m -= 1
    return dummy.next


def print_list(head):
    while head:
        print(head.val, end="->")
        head = head.next
    print("None")


def list_to_array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr


def test1():
    L = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    result = delete_n_after_m(L, m=2, n=1)
    assert list_to_array(result) == [1,2,4,5]
    print("test 1 successful")


def test2():
    L = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    result = delete_n_after_m(L, m=0, n=2)
    assert list_to_array(result) == [3,4,5]
    print("test 2 successful")


def test3():
    L = None
    result = delete_n_after_m(L, m=0, n=2)
    assert list_to_array(result) == []
    print("test 3 successful")


def test4():
    L = Node(1, Node(2, Node(3)))
    result = delete_n_after_m(L, m=1, n=0)
    assert list_to_array(result) == [1, 2, 3]
    print("test 4 successful")


def test5():
    L = Node(1, Node(2, Node(3)))
    result = delete_n_after_m(L, m=2, n=1)
    assert list_to_array(result) == [1, 2]
    print("test 5 successful")


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
