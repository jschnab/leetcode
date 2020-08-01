# leetcode challenge 86: partition linked list
# given a linked list and a value x, return a linked list where the nodes
# with value < x precede nodes with value >= x
# the relative order of nodes in each partition should be preserved
# input: 1 -> 4 -> 3 -> 2 -> 5 -> 2
# output: 1 -> 2 -> 2 -> 4 -> 3 -> 5


class Node:
    def __init__(self, val=None, next_=None):
        self.val = val
        self.next = next_


def partition(head, x):
    """
    Partition the linked list based on node value.

    Time complexity: O(n)
    Space complexity: O(1)

    We have a space complexity of 1 since we reorganize the links between
    nodes.

    We create two pointers to the head of two linked lists:
    - a list which contains nodes with value < x
    - a list which contains nodes with value >= x

    We iterate through the input linked list and add nodes to each of the
    two new linked lists. Then we join the two new linked lists and return.

    :param Node head: first node of linked list
    :param int: partition value
    :returns: first node of the partition linked list
    """
    head_before = Node()
    before = head_before
    head_after = Node()
    after = head_after

    while head:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next

    # end the list
    after.next = None

    # join the two lists together
    before.next = head_after.next

    return head_before.next


def test1():
    L = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))
    result = partition(L, 3)
    array = []
    while result:
        array.append(result.val)
        result = result.next
    assert array == [1, 2, 2, 4, 3, 5]
    print("test 1 successful")


if __name__ == "__main__":
    test1()
