# from the book "cracking the code interview"
# given an unsorted linked list, remove duplicates


class Node:
    def __init__(self, val=None, next_=None):
        self.val = val
        self.next = next_


def remove_dup_unsorted(head):
    """
    Remove duplicates from an unsorted linked list, leaving only nodes
    with unique values.

    Time complexity: O(n) as we iterate once through the list
    Space complexity: O(1) as we operate on the linked list in place

    :param Node head: head of the linked list
    :return Node: head of the de-duplicated linked list
    """
    seen = {}
    first = Node(next_=head)
    current = first.next

    while current:
        seen[current.val] = 1
        if current.next and seen.get(current.next.val):
            current.next = current.next.next
        current = current.next

    return first.next


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def test1():
    head = Node(6, Node(2, Node(3, Node(3))))
    dedup = remove_dup_unsorted(head)
    assert to_list(dedup) == [6, 2, 3]
    print("test 1 successful")


def test2():
    head = Node(3, Node(1, Node(1, Node(2))))
    dedup = remove_dup_unsorted(head)
    assert to_list(dedup) == [3, 1, 2]
    print("test 2 successful")


def test3():
    head = Node(4, Node(4, Node(0, Node(2))))
    dedup = remove_dup_unsorted(head)
    assert to_list(dedup) == [4, 0, 2]
    print("test 3 successful")


def test4():
    head = Node(5, Node(5, Node(3, Node(3, Node(9, Node(9))))))
    dedup = remove_dup_unsorted(head)
    assert to_list(dedup) == [5, 3, 9]
    print("test 4 successful")


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
