"""
leetcode 2540: minimum common value

Given two integer arrays A and B, sorted in non-decreasing order, return the
minimum integer common to both arrays. If there is not common integer amongst A
and B, return -1.
"""

def min_com(A, B):
    """
    Since arrays are already sorted, we compare array elements pairs with
    increasing indexes until we eventually find one that is equal.
    """
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
        else:
            return A[i]  # A[i] == B[i]
    return -1


def min_com2(A, B):
    """
    We can determine the set intersection of A and B, then find the minimum.
    """
    return min(set(A) & set(B), default=-1)


def test1():
    assert min_com([1, 2, 3], [2, 4]) == 2
    assert min_com2([1, 2, 3], [2, 4]) == 2
    print("test 1 successful")


def test2():
    assert min_com([1, 2, 3, 6], [2, 3, 4, 5]) == 2
    assert min_com2([1, 2, 3, 6], [2, 3, 4, 5]) == 2
    print("test 2 successful")


def test3():
    assert min_com([1, 6], [2, 3, 4, 5]) == -1
    assert min_com2([1, 6], [2, 3, 4, 5]) == -1
    print("test 3 successful")


if __name__ == "__main__":
    test1()
    test2()
    test3()
