# leetcode problem 234: determine if linked list is palindrome
# input: 1->2->3
# output: False
#
# input: 1->2->3->2->1
# output: True


class Node:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def is_palindrome2(head):
    """
    Check if a linked list is a palindrome.

    :param Node head: first node of the list
    :returns: bool - True if list is palindrome else False
    """
    if not head:
        return True
    # position the slow "pointer" on the middle node
    slow = head
    fast = head
    while fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the linkage of nodes after the middle node
    reverse = None
    while slow:
        next_ = slow.next
        slow.next = reverse
        reverse = slow
        slow = next_

    # iterate from beginning and end and check node values for equality
    while reverse:
        if head.val != reverse.val:
            return False
        head = head.next
        reverse = reverse.next
    return True


def is_palindrome(head):
    """
    :param Node head: first node of linked list
    :return bool: True if linked list is palindrome else False

    Time complexity: O(n)
    Space complexity: O(n)
    """
    # convert the linked list to an array
    array = []
    current = head
    length = 0
    while current:
        array.append(current.val)
        length += 1
        current = current.next

    # return array == array[::-1]
    i = 0
    j = length - 1
    while i < j:
        if array[i] != array[j]:
            return False
        i += 1
        j -= 1
    return True


def test1():
    L = Node(1, Node(2, Node(3, Node(2, Node(1)))))
    assert is_palindrome2(L) is True
    print("test 1 successful")


def test2():
    L = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    assert is_palindrome2(L) is False
    print("test 2 successful")


def test3():
    L = None
    assert is_palindrome2(L) is True
    print("test 3 successful")


if __name__ == "__main__":
    test1()
    test2()
    test3()
