"""
leetcode 2358: maximum number of groups entering a competition

We are given a positive integer array A which represents the grades of students
in a university. We would like to enter all students int a competition in
ordered non-empty groups, such that the ordering meets the following
conditions:

* the sum of the grades of students in the ith group is less than the sum of
  the grades of students in the (i + 1)th group, for all groups except the last
* the total number of students in the ith group is less than the total number
  of students in the (i + 1)th group, for all groups except the last

Return the maximum number of groups that can be formed.
"""


def groups(A):
    """
    We sort the array, then make groups with 1, 2, 3, etc. elements starting
    from the beginning. This satisfies the second condition. To also satisfy
    the first condition, we may have to merge the last two groups.
    """
    A.sort()
    # i represents the start index of groups, and is also the number of groups.
    i = 1
    # j represents the end index of groups.
    j = 1
    while j <= len(A):
        i += 1
        j += i
    # If the last group is not full, we have to merge it with the previous
    # group, and we have i - 1 groups, else we have i groups.
    if j > len(A):
        return i - 1
    return i


def test1():
    assert groups([10, 6, 12, 7, 3, 5]) == 3
    print("test 1 successful")


def test2():
    assert groups([8, 8]) == 1
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
