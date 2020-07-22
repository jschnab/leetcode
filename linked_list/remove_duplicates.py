# leetcode challenge 82: remove duplicates from sorted list II
# given a sorted linked list, delete all nodes that have duplicate number,
# leaving only distinct numbers from the original list
# input: 1->2->3->3->4->4->5
# output: 1->2->5


class Node:
    def __init__(self, value, next_):
        self.value = value
        self.next = next_


def remove_duplicates(head):
    """
    :param Node head: first node of the linked list
    :return Node: first node of the linked list
    """
    first = Node(None, head)
    lag = first
    lead = head

    while lead and lead.next:

        # if we detect a duplicate
        if lead.value == lead.next.val:

            # move the lead node to the first node after duplicates
            # and update the next pointer of lag to point to lead
            # but don't move the lag node yet
            while lead.next and lead.value == lead.next.value:
                lead = lead.next
            lead = lead.next
            lag.next = lead

        # we are past duplicates, move both pointers forward
        else:
            lag = lag.next
            lead = lead.next

    return first.next
