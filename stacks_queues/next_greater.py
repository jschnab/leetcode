# leetcode challenge 496: next greater element I
# given two arrays without duplicates A1 and A2 where A1 elements
# are a subset of A2
# find the next greater elements of A1 in A2, or return -1 if not exists

# input: A1 = [4, 1, 2] A2 = [1, 3, 4, 2]
# output: [-1, 3, -1]

# input: A1 = [2, 4] A2 = [1, 2, 3, 4]
# output: [3, -1]


def next_greater(A1, A2):
    """
    Find the next greater element.

    Time complexity: O(n^2) because we iterate through remaining elements
                     for each element
    Space complexity: O(n) we store the results in a list of size n

    :param list[int] A1:
    :param list[int] A2:
    :returns: list[int]
    """
    result = []
    for i in A1:
        appended = False
        for j in A2[A2.index(i):]:
            if j > i:
                result.append(j)
                appended = True
                break
        if not appended:
            result.append(-1)

    return result


def next_greater2(A1, A2):
    """
    Find the next greater element.

    Time complexity: O(n) we iterate through A1 then through A2 sequentially
    Space complexity: O(n) we store the results in a list of size n

    :param list[int] A1:
    :param list[int] A2:
    :returns: list[int]
    """
    result = []
    stack = []
    next_greater = {}

    # we first store v the next greater element than k in a dictionary {k: v}
    # all elements are stored in a stack and we compare stack elements to
    # following elements to find the next greater, if found we pop
    for n in A2:
        while stack and stack[-1] < n:
            next_greater[stack.pop()] = n
        stack.append(n)

    # we build results by checking if we have found a greater element, if not
    # we add -1 to the results
    for n in A1:
        result.append(next_greater.get(n, -1))

    return result


def test1():
    A1 = [4, 1, 2]
    A2 = [1, 3, 4, 2]
    assert next_greater(A1, A2) == [-1, 3, -1]
    print("test 1 successful")


def test2():
    A1 = [4, 1, 2]
    A2 = [1, 3, 4, 2]
    assert next_greater2(A1, A2) == [-1, 3, -1]
    print("test 2 successful")


def test3():
    A1 = [2, 4]
    A2 = [1, 2, 3, 4]
    assert next_greater(A1, A2) == [3, -1]
    print("test 3 successful")


def test4():
    A1 = [2, 4]
    A2 = [1, 2, 3, 4]
    assert next_greater2(A1, A2) == [3, -1]
    print("test 4 successful")


def main():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    main()
