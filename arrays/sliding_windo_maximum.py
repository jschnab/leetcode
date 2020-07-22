from collections import deque

# leetcode 239
# sliding window maximum

# given an array of numbers 'nums', return the maximum of every subarray
# of nums of size k


def maximum_sliding_window_brute(nums, k):
    """
    Brute force solution

    Time complexity: O(nk)
    Space complexity: O(n)

    :param list[int] nums: array of integers
    :param int k: size of the sliding window
    """
    answer = []
    for i in range(k-1, len(nums)):
        answer.append(max(nums[i-k+1:i+1]))
    return answer


def maximum_sliding_window(nums, k):
    """
    Iterate over elements and enqueue their index.
    At each iteration perform these four steps:
    1. pop from the queue the indexes of elements smaller than the current
    2. append the current index
    3. remove from the queue elements outside the window
    4. if we are at or past the (k-1)th element then record the maximum of
       the window

    Time complexity: O(n)
    Space complexity: O(n)

    :param list[int] nums: array of integers
    :param int k: size of the sliding window
    """
    output = []
    q = deque()
    for i, n in enumerate(nums):
        while q and nums[q[-1]] < n:
            q.pop()
        q.append(i)
        if q[0] == i - k:
            q.popleft()
        if i >= k - 1:
            output += nums[q[0]],
    return output


if __name__ == "__main__":
    maxi = maximum_sliding_window([1, 3, -1, -3, 5, 4, 6, 7], 3)
    print(maxi)
