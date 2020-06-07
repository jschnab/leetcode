# leetcode problem 203
# remove elements with specific value from linked list
# for example:
# remove 4 from [1, 2, 3, 4] returns [1, 2, 3]
# remove 1 from [1, 1] returns []


class Node:
    def __init__(self, val, _next=None):
        self.val = val
        self.next = _next


def delete_elements(head, val):
    dummy = Node(None, head)
    current = dummy
    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
    return dummy.next


def get_values(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def test1():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    if get_values(head) == [1, 2, 3]:
        print("test 1 succeeded")
    else:
        print("test 1 failed")


def test2():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    if get_values(delete_elements(head, 3)) == [1, 2]:
        print("test 2 succeeded")
    else:
        print("test 2 failed")


def test3():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    if get_values(delete_elements(head, 1)) == [2, 3]:
        print("test 3 succeeded")
    else:
        print("test 3 failed")


def test4():
    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(1)
    if get_values(delete_elements(head, 1)) == []:
        print("test 4 succeeded")
    else:
        print("test 4 failed")


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
