class Node:
    def __init__(self, val=None, next_=None):
        self.val = val
        self.next = next_


def reverse(head):
    rev = None
    while head:
        next_node = head.next
        head.next = rev
        rev = head
        head = next_node
    return rev


def print_list(head):
    while head:
        print(head.val, end="->")
        head = head.next
    print("None")


if __name__ == "__main__":
    linked_list = Node(1, Node(2, Node(3)))
    reverse = reverse(linked_list)
    print_list(reverse)
