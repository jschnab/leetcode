# script which implements a class for linked lists

class ListNode(object):
    """Class for linked lists."""
    def __init__(self, value):
        self.val = value
        self.next = None

    def reverse(self, head):
        """Reverse linked list.
        Time complexity O(n)
        Space complexity O(1)."""
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reverse_recur(self, head):
        """Recursion algorithm to reverse linked list.
        Time complexity O(n)
        Space complexity O(n).

        The list is n(1),..., n(k-1), n(k), n(k+1),...n(m)
        Let's assume n(k+1) to n(m) has been reversed and we are at node k.
        We want n(k+1) to point to n(k), so n(k).next.next = n(k)"""
        if head == None or head.next == None:
            return head
        p = self.reverse_recur(head.next)
        head.next.next = head
        head.next = None
        return p

    def get_elements(self, head):
        elements = []
        while head:
            elements.append(head.val)
            head = head.next
        return elements

    def remove_duplicates(self, head):
        """Remove duplicates from linked list."""
        cur = head
        d = {} #dictionary to store values already seen
        while cur and cur.next:
            d[cur.val] = 1
            if not d.get(cur.next.val):
                cur = cur.next
            else:
                cur.next = cur.next.next
        return head

    def odd_even_linkedlist(self, head):
        """Sort nodes of linked list with odd nodes first then even nodes.

        Parameter:
        head (ListNode): head to a linked list where values are incremental
                         integers (e.g. 1 -> 2 -> 3 -> 4 -> 5 -> NULL)

        Returns:
        ListNode: head to list with sorted nodes (i.e. 1 -> 3 -> 5 -> 2 -> 4 -> NULL)
        """
        cur = head
        headEven = cur.next
        curEven = headEven
        while cur.next:
            cur.next = cur.next.next
            if cur.next:
                cur = cur.next
                curEven.next = cur.next
                curEven = curEven.next
            else:
                break
        cur.next = headEven
        return head

    def hasCycle(self, head):
        """Returns True if linked list has cycle else False."""
        if not head or not head.next:
            return False
        slow = head.next
        fast = head.next.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

if __name__ == '__main__':
    head = ListNode(1)
    cur = head
    for i in range(2, 7):
        cur.next = ListNode(i)
        cur = cur.next
