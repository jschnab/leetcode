from collections import deque

# leetcode 1438
# get the length of the longest continuous subarray with the absolute
# difference between two elements is less or equal to some limit
# array = [8,2,4,7]
# limit = 4
# answer = 2
# [2, 4] and [4, 7] are the longest arrays satisfying these conditions

def longest_subarray(array, limit):
    """
    We will keep track of arrays satisfying the conditions using a FIFO queue
    which we will adjust depending on new elements.

    Time complexity: O(N)
    Space complexity: O(N)
    """
    answer = 0  # length of the longest subarray
    maxi = array[0]  # keep track of greatest element
    mini = array[0]  # keep track of the smallest element
    q = deque()  # FIFO queue to keep track of longest array

    for a in array:
        q.append(a)
        if a > maxi:
            maxi = a
        elif a < mini:
            mini = a

        # if the condition is satisfied for the maximum and minimum elements,
        # it is satisfied for all
        while (maxi - mini) > limit:
            # adjust the queue to keep satisfying the condition
            old = q.popleft()
            # we may have to ajust recorded maximum and minimum
            if old == maxi:
                maxi = max(array)
            if old == mini:
                mini = min(array)

        answer = max(answer, len(q))

    return answer
