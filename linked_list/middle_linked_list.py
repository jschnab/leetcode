# script which converts a list to a linked list
# then returns the list elements from the middle to the end

class ListNode(object):
    """Class which implements a linked list."""
    def __init__(self, value):
        self.val = value
        self.next = None

def list_to_linkedlist(lis):
    """Takes a list and returns a linked list."""
    root = ListNode(0)
    ptr = root
    for n in lis:
        ptr.next = ListNode(n)
        ptr = ptr.next
    ptr = root.next
    return ptr

def mid_linkedlist(linked):
    """Takes a linked list and returns a list started from the middle
of the linked list."""
    l = [linked]
    while l[-1].next:
        l.append(l[-1].next)
    return l[len(l) // 2]

def linkedlist_to_list(linked):
    lis = []
    while linked != None:
        lis.append(linked.val)
        linked = linked.next
    return lis

if __name__ == '__main__':
    mylist = list(map(int, input().split()))
    linked = list_to_linkedlist(mylist)
    mid = mid_linkedlist(linked)
    print(linkedlist_to_list(mid))
