# sum two linked lists stored in reverse order (don't forget carry-over)
# [3 -> 4 -> 2] + [5 -> 6 -> 4] = [7 -> 0 -> 8] so return [8 -> 0 -> 7]

from middle_linked_list import *

class Solution(object):
    def add_two(self, l1, l2):

        # ListNode instance which we'll return
        dummyHead = ListNode(0)
        # ListNode instance storing the current value
        answer = dummyHead
        carry = 0

        # iterate through input linked lists
        # get value of current node, or 0 if we reached the end
        while l1 or l2:
            if l1: x = l1.val
            else: x = 0
            if l2: y = l2.val
            else: y = 0
        
            # calculate sum and carry
            S = x + y + carry
            carry = S // 10

            # append current sum to answer
            answer.next = ListNode(S % 10)
            answer = answer.next

        # add eventual last carry as last node
        if carry > 0:
            answer.next = ListNode(carry)

        # remember head is 0
        return dummyHead.next
