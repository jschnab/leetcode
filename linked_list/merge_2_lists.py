# leetcode.com/problems/merge-two-sorted-lists/
# problem 21
#
# merge two sorted linked lists and return a new linked list
# input: l1 = [1, 2, 4], l2 = [1, 3 4]
# output: [1, 1, 2, 3, 4, 4]

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


def my_merge_2_lists_(l1: ListNode, l2: ListNode) -> ListNode:
    """
    My own iterative solution.
    m is length of l1, n is length of l2
    space complexity: O(m + n)
    time complexity: O(m + n)
    """
    # if one of the lists is empty return the other one
    if not l1:
        return l2
    if not l2:
        return l1

    # initialize the output with the smallest node
    if l1.val <= l2.val:
        output = l1
        l1 = l1.next
    else:
        output = l2
        l2 = l2.next

    # save the head of the output to be returned
    cur_output = output

    # loop until both lists are exhausted
    while True:
        if not l1 and not l2:
            break
        if l1:
            if l2:
                if l1.val <= l2.val:
                    cur_output.next = l1
                    l1 = l1.next
                else:
                    cur_output.next = l2
                    l2 = l2.next
            else:
                cur_output.next = l1
                l1 = l1.next
        else:
            # we are just left with l2
            cur_output.next = l2
            l2 = l2.next

    return output


def merge_2_lists(l1: ListNode, l2: ListNode):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1 > l2:
            cur.next = l2
            l2 = l2.next
        else:
            cur.next = l1
            l1 = l1.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next


def merge_2_lists_recursive(l1, l2):
    """
    Recursive solution.
    """
    if l1 and l2:
        # make sure l1 is the one starting with smallest node
        if l1.val > l2.val:
            l1, l2 = l2, l1
        # merge remainders behind smallest node
        l1.next = merge_2_lists_recursive(l1.next, l2)
    # base case - if l1 or l2 or both are empty, return what's there
    return l1 or l2
