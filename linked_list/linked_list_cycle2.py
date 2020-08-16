# leetcode challeng 142: linked list cycle II
# given a linked list, return the node where the cycle begins
# if there is no cycle, return None

# input: 3 -> 2 -> 0 -> 4
#             ^---------'
# output: 2


class Node:
    def __init__(self, val=None, next_=None):
        self.val = val
        self.next = next_


def get_cycle(head):
    nodes = {}
    while head:
        if nodes.get(head):
            return head
        nodes[head] = 1
        head = head.next


def test1():
    node_a = Node(3)
    node_b = Node(2)
    node_c = Node(0)
    node_d = Node(-4)
    node_a.next = node_b
    node_b.next = node_c
    node_c.next = node_d
    node_d.next = node_b
    assert get_cycle(node_a) == node_b
    print("test 1 successful")


def test2():
    node_a = Node(1)
    node_b = Node(2)
    node_a.next = node_b
    assert get_cycle(node_a) == None
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
