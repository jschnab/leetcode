# leetcode challenge 1019: next greater node in linked list
# given a linked list, return an array of integers which represent,
# for each linked list index, the index of the next greater node

# input:  2->1->5
# output: 5, 5, 0

# input:  1->7->5->1->9->2->5->1
# output: 7, 9, 9, 9, 0, 5, 0, 0


class Node:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


def next_greater(head):
    """
    Return the list of the next greater node for each node index.

    Time complexity: O(n^2)
    Space complexity: O(n)

    :param Node head: first node of the list
    :return list[int]: indices of next greater nodes
    """
    result = []
    while head:
        current_val = head.val
        current = head.next
        found_greater = False
        while current:
            if current.val > current_val:
                result.append(current.val)
                found_greater = True
                break
            current = current.next
        if not found_greater:
            result.append(0)
        head = head.next
    return result


def next_greater2(head):
    """
    Return the list of the next greater node for each node index.

    Time complexity: O(n)
    Space complexity: O(n)

    :param Node head: first node of the list
    :return list[int]: indices of next greater nodes
    """
    result = []
    stack = []
    while head:
        while stack and stack[-1][1] < head.val:
            result[stack.pop()[0]] = head.val
        stack.append([len(result), head.val])
        result.append(0)
        head = head.next
    return result
