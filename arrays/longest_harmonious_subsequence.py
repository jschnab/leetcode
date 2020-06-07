# leetcode problem 594
# harmonious array: difference between max and min is exactly 1
# given an array of integers, find the length of the longest harmonious
# subsequence given all possible subsequences


def longest_harmonious_subsequence(array):
    """
    :param list[integer] array: array of integers
    :return int: length of longest harmonious subsequence

    Time complexity: O(n)
    Space complexity: O(n)

    We achieve linear time complexity with a hash map which stores the number
    of occurrences of every element. We iterate once through the array to
    generate the hash map and then again once through the hash map to count
    the number of elements consistent with harmonicity.
    """
    answer = 0

    # get counts of each element
    counts = {}
    for i in array:
        counts[i] = counts.get(i, 0) + 1

    # add count of element and element + 1 (harmonious rule)
    for key in counts:
        if counts.get(key + 1):
            answer = max(answer, counts[key] + counts[key + 1])

    return answer


def longest_harmonious_subsequence2(array):
    """
    :param list[integer] array: array of integers
    :return int: length of longest harmonious subsequence

    Time complexity: O(n2)
    Space complexity: O(n)

    We iterate through the array, and iterate within the first iteration
    to find elements which are consistent with harmononicty.
    """
    answer = 0
    for i in array:
        count = 0
        is_harmonious = False
        for j in array:
            if i == j:
                count += 1
            elif i == j + 1:
                count += 1
                is_harmonious = True
        if is_harmonious:
            answer = max(answer, count)
    return answer


def test1():
    array = [1, 3, 2, 2, 5, 2, 3, 7]
    if longest_harmonious_subsequence(array) != 5:
        print("test 1 failed")
    else:
        print("test 1 succeeded")


def test2():
    array = [1, 2, 3, 4]
    if longest_harmonious_subsequence(array) != 2:
        print("test 2 failed")
    else:
        print("test 2 succeeded")


def test3():
    array = [1, 1, 1, 1]
    if longest_harmonious_subsequence(array) != 0:
        print("test 3 failed")
    else:
        print("test 3 succeeded")


def test4():
    array = []
    if longest_harmonious_subsequence(array) != 0:
        print("test 4 failed")
    else:
        print("test 4 succeeded")


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
