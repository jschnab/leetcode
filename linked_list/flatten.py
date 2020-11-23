# flatten a singly linked list
# a nested linked list is stored in the "child" pointer of a node


class Node:
    def __init__(self, val=None, next_=None, child=None):
        self.val = val
        self.next = next_
        self.child = child


def flatten(node):
    if not node:
        return
    while node:
        previous = node
        if node.child:
            last_child = flatten(node.child)
            next_ = node.next
            last_child.next = next_
            node.next = node.child
            node.child = None
        node = node.next
    return previous


def print_list(head):
    while head:
        if head.next:
            print(f"{head.val}->", end="")
        else:
            print(head.val)
        head = head.next


def check_children(head):
    while head:
        if head.child:
            raise ValueError(f"node {head.val} has child")
        head = head.next


def to_array(head):
    array = []
    while head:
        array.append(head.val)
        head = head.next
    return array


def test1():
    head = Node(
        1,
        Node(
            2,
            Node(3),
            Node(
                4,
                Node(5),
            )
        ),
    )
    flatten(head)
    assert to_array(head) == [1, 2, 4, 5, 3]
    check_children(head)
    #print_list(head)
    print("test 1 successful")


def test2():
    head = Node(
        1,
        Node(2),
        Node(
            3,
            Node(4)
        ),
    )
    flatten(head)
    assert to_array(head) == [1, 3, 4, 2]
    check_children(head)
    #print_list(head)
    print("test 2 successful")


def test3():
    head = Node(
        1,
        None,
        Node(
            2,
            None,
            Node(3)
        )
    )
    flatten(head)
    assert to_array(head) == [1, 2, 3]
    check_children(head)
    #print_list(head)
    print("test 3 successful")


def test4():
    head = Node(
        1,
        Node(
            2,
            Node(3),
            Node(
                4,
                Node(
                    5,
                    Node(6),
                    Node(7)
                ),
            ),
        ),
    )
    flatten(head)
    #print_list(head)
    assert to_array(head) == [1, 2, 4, 5, 7, 6, 3]
    check_children(head)
    print("test 4 successful")


def test5():
    head = None
    flatten(head)
    assert to_array(head) == []
    print("test 5 successful")


def test6():
    head = Node(
        1,
        Node(
            2,
            Node(3),
        ),
    )
    flatten(head)
    assert to_array(head) == [1, 2, 3]
    check_children(head)
    print("test 6 successful")


def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()


if __name__ == "__main__":
    main()
