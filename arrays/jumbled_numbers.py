"""
Given an array which represents a mapping rule of shuffled digits.
mapping[i] = j means that digit i should be mapped to digit j.

The mapped value of an integer is the new integer obtained by replacing each
occurence of digit i in the integer with mapping[i] for 0 <= i <= 9.

Given an array of integers, sort this array based on the mapped values of its
items. The sorted array contains the original values, not the mapped ones.

Sorting should be stable, meaning that integers with the same mapped value
should appear in the output with the same order as in the input.
"""


def sort_jumbled(A, mapping):
    """
    """
    def map_int(x, mapping):
        """
        Return the mapped value of x.
        """
        stack = []
        if x == 0:
            stack = [mapping[0]]
        while x > 0:
            stack.append(mapping[x % 10])
            x //= 10
        result = 0
        while stack:
            result *= 10
            result += stack.pop()
        return result

    arr = [(x, map_int(x, mapping)) for x in A]
    arr.sort(key=lambda tup: tup[1])
    return [x[0] for x in arr]


def test1():
    A = [991, 338, 38]
    mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
    expected = [338, 38, 991]
    assert sort_jumbled(A, mapping) == expected
    print("test 1 successful")


def test2():
    A = [789, 456, 123]
    mapping = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = [123, 456, 789]
    assert sort_jumbled(A, mapping) == expected
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
