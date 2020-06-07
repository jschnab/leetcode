# problem 674
# given an unsorted array, return the length of the longest
# increasing subarray (continuous subsequence)


def longest_increasing(array):
    """
    :param list array: list of orderable elements
    :return int: length of longest increasing subarray

    Time complexity: O(n)
    Space complexity: O(1)
    """
    if not array:
        return 0
    answer = 1
    count = 1
    for i in range(1, len(array)):
        if array[i - 1] < array[i]:
            count += 1
            answer = max(answer, count)
        else:
            count = 1
    return answer
