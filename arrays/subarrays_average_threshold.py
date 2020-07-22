from collections import deque

# leetcode problem 1343
# given an array of integers and two integers k and threshold
# return the number of subarrays of size k with average greater than or
# equal to threshold


def subarrays_average_threshold(arr, k, threshold):
    """
    Time complexity: O(n)
    Space complexity: O(k)

    :param list[int] arr: array of integers
    :param int k: window size
    :param int threshold: threshold
    """
    sub = deque()
    total = 0
    count = 0
    length = 0

    for n in arr:
        sub.append(n)
        total += n
        length += 1
        if length > k:
            total -= sub.popleft()
            length -= 1
        if length == k and total / k >= threshold:
            count += 1

    return count


if __name__ == "__main__":
    count = subarrays_average_threshold(
        [2, 2, 2, 2, 5, 5, 5, 8],
        3,
        4
    )
    print(count)
