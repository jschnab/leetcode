"""
leetcode #2148

Given an array of integers, we want to determine the number of elements that
have both a strictly smaller and strictly greater element in the array.
"""


def count_elements(arr):
    """
    We solve the challenge in linear time and constant space by determining
    the minimum and maximul elements of the array then comparing each element
    of the array to these extrema.

    :param list[int] arr: Array of integers.
    :returns (int): Number of items satisfying the challenge description.
    """
    mini = min(arr)
    maxi = max(arr)
    result = 0
    for i in arr:
        if mini < i < maxi:
            result += 1
    return result


def test1():
    assert count_elements([11, 7, 2, 15]) == 2
    print("test 1 successful")


def test2():
    assert count_elements([-3, 3, 3, 90]) == 2
    print("test 2 successful")


def test3():
    assert count_elements([1, 2]) == 0
    print("test 3 successful")


def test4():
    assert count_elements([1, 2, 1]) == 0
    print("test 4 successful")


def main():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    main()
