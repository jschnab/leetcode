# problem 1290: convert a linked list storing bits into an integer
# input: 1->0->1
# output: 5


class Node:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def bin_to_int(head):
    """
    :param Node head: first node of linked list
    :return int: linked list converted to integer

    Time complexity: O(n)
    Space complexity: O(1)
    """
    answer = 0
    while head:
        answer = answer * 2 + head.val
        head = head.next
    return answer


def test1():
    L = Node(1, Node(0, Node(1)))
    assert bin_to_int(L) == 5
    print("test 1 successful")


def test2():
    L = Node(1, Node(0, Node(1, Node(1))))
    assert bin_to_int(L) == 11
    print("test 2 successful")


if __name__ == "__main__":
    test1()
    test2()
