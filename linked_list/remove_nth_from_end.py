# leetcode problem 19
# remove the nth node of a linked list, starting from the end
# for example:
# [1,2,3] and n = 2 return [1,3]
# [1,2,3] and n = 3 return [2,3]
# [1] and n = 1 return []


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def remove_nth(head, n):
    """
    We'll two pointers.
    We'll traverse the list once, giving a time complexity of O(n).
    Let's assume the value of n is always valid (less than length of list).
    """
    if not head:
        return
    # we use an additional node upstream to make this easier
    dummy = Node()
    dummy.next = head
    i = dummy
    j = head

    # we'll keep pointer j ahead of i by n + 1 steps
    for _ in range(n):
        j = j.next
    while j:
        j = j.next
        i = i.next

    # delete nth element
    i.next = i.next.next

    return dummy.next


def get_values(head):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result


def test1():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    result = remove_nth(head, 2)
    if get_values(result) != [1, 3]:
        print("Test 1 failed")
    else:
        print("Test 1 succeeded")


def test2():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    result = remove_nth(head, 3)
    if get_values(result) != [2, 3]:
        print("Test 2 failed")
    else:
        print("Test 2 succeeded")


def test3():
    head = Node(1)
    result = remove_nth(head, 1)
    if get_values(result) != []:
        print("Test 3 failed")
    else:
        print("Test 3 succeeded")


if __name__ == "__main__":
    test1()
    test2()
    test3()
