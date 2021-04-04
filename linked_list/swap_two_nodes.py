# swap two nodes in a linked list: leetcode 1721

# given the head node of a linked list, and a number k, swap the values
# of the kth node from the start and the kth node from the end (index starts
# at 1)


class Node:
    def __init__(self, value=0, next_=None):
        self.val = value
        self.next = next_


def swap_nodes(head, k):
    lead = head
    for _ in range(k-1):
        lead = lead.next
    left = lead

    right = head
    while lead.next != None:
        lead = lead.next
        right = right.next

    left.val, right.val = right.val, left.val

    return head


def get_list(head):
    lst = []
    while head != None:
        lst.append(head.val)
        head = head.next
    return lst


def test1():
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    head = swap_nodes(head, 2)
    assert get_list(head) == [1, 4, 3, 2, 5]


def test2():
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    head = swap_nodes(head, 3)
    assert get_list(head) == [1, 2, 3, 4, 5]


def test3():
    head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    head = swap_nodes(head, 5)
    assert get_list(head) == [5, 2, 3, 4, 1]




def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
