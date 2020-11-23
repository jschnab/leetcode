# leetcode challenge 430: flatten a doubly linked list
# a nested linked list is stored in the "child" pointer of a node


class Node:
    def __init__(self, val=None, next_=None, prev=None, child=None):
        self.val = val
        self.next = next_
        self.prev = prev
        self.child = child


def flatten_recur(node):
    if not node:
        return

    while node:
        if node.child:
            last_child = flatten(node.child)
            next_ = node.next
            node.next = node.child
            node.child.prev = node
            last_child.next = next_
            if next_:
                next_.prev = last_child
            node.child = None

        previous = node
        node = node.next

    return previous


def flatten(head):
    if not head:
        return

    prev = None
    stack = [head]

    while stack:
        cur = stack.pop()
        cur.prev = prev
        if prev:
            prev.next = cur

        if cur.next:
            stack.append(cur.next)
            cur.next = None

        if cur.child:
            stack.append(cur.child)
            cur.child = None

        prev = cur


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
            print(f"error: node {head.val} has child")
        head = head.next


def check_prev(head):
    found_errors = False
    prev = None
    while head:
        if prev:
            if head.prev != prev:
                found_errors = True
                if not head.prev:
                    print(f"error: {head.val}->prev is None")
                else:
                    print(
                        f"error: ({head.val})->prev = {head.prev.val} "
                        f"(expected {prev.val})"
                    )
        prev = head
        head = head.next
    assert not found_errors


def to_array(head):
    array = []
    while head:
        array.append(head.val)
        head = head.next
    return array


def test1():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    one.next = two
    two.prev = one
    two.next = three
    three.prev = two
    flatten(one)
    assert to_array(one) == [1, 2, 3]
    check_children(one)
    check_prev(one)
    #print_list(one)
    print("test 1 successful")


def test2():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    one.next = two
    two.prev = one
    two.next = three
    two.child = four
    three.prev = two
    four.next = five
    five.prev = four
    flatten(one)
    assert to_array(one) == [1, 2, 4, 5, 3]
    check_children(one)
    check_prev(one)
    #print_list(one)
    print("test 2 successful")


def test3():
    head = None
    flatten(head)
    assert to_array(head) == []
    print("test 3 successful")


def test4():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    one.child = two
    two.child = three
    flatten(one)
    assert to_array(one) == [1, 2, 3]
    check_children(one)
    check_prev(one)
    #print_list(one)
    print("test 4 successful")


def test5():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    one.next = two
    two.prev = one
    two.next = three
    two.child = four
    three.prev = two
    four.next = five
    five.prev = four
    five.next = six
    five.child = seven
    six.prev = five
    flatten(one)
    #print_list(one)
    assert to_array(one) == [1, 2, 4, 5, 7, 6, 3]
    check_children(one)
    check_prev(one)
    print("test 5 successful")


def main():
    test1()
    test2()
    test3()
    test4()
    test5()


if __name__ == "__main__":
    main()
