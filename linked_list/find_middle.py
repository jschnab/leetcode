# from "cracking the coding interview"
# find the middle node of a linked list


class Node:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def find_middle(head):
    """
    Find the middle node of a linked list.

    Time complexity: O(n) we iterate once through the list
    Space complexity: O(1) we store only two "pointers"

    :param Node head: first node of the list
    :returns: Node - middle element
    """
    if not head:
        return
    lead = head
    lag = head
    # we check lead.next.next to get the "floor" middle element
    while lead.next and lead.next.next:
        lead = lead.next.next
        lag = lag.next
    return lag


def array_to_list(array):
    """
    Take an array and return a linked list.
    """
    dummy = Node()
    current = dummy
    for i in array:
        current.next = Node(i)
        current = current.next
    return dummy.next


def print_list(head):
    """
    Pretty prints a linked list.
    """
    while head:
        if head.next:
            print(head.val, "-> ", end="")
        else:
            print(head.val)
        head = head.next


def test_1():
    head = array_to_list([1, 2, 3])
    print_list(head)
    print("middle:", find_middle(head).val)


def test_2():
    head = array_to_list([1, 2, 3, 4])
    print_list(head)
    print("middle:", find_middle(head).val)


def main():
    test_1()
    test_2()


if __name__ == "__main__":
    main()
