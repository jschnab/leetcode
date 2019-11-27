# script which determines if two linked lists have an intersection
# i.e. merge at some node

class ListNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None

def intersect(A, B):
    """Determine if two linked lists intersect.
    If two linked lists have an intersection, their nodes are the same after it.
    A + B have the sale "tail" as B + A."""

    ptA = A
    ptB = B
    jumpNext = False
    
    while ptA and ptB:
        if ptA == ptB:
            return ptA
        ptA, ptB = ptA.next, ptB.next

        if not ptA and not jumpNext:
            ptA, jumpNext = B, True

        if not ptB:
            ptB = A
    return

if __name__ == '__main__':
    A = ListNode(4)
    A.next = ListNode(1)
    A.next.next = ListNode(8)
    A.next.next.next = ListNode(4)
    B = ListNode(5)
    B.next = ListNode(0)
    B.next.next = ListNode(1)
    B.next.next.next = A.next.next
    # the intersection is node 8
