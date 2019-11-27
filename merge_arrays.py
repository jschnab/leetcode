def merge_sorted_arrays(a1, m, a2, n):
    """
    Merge a2 into a1 in place, a1 has placeholders at its tail
    to accomodate all elements.

    :param list a1: array 1
    :param int m: number of elements in a1 (excluding placeholders)
    :param list a2: array 2
    :param int n: number of elements in a2
    """
    # we iterate over list elements from the end (since they are sorted)
    # and fill a1 by the end
    while m > 0 and n > 0:
        if a1[m-1] > a2[n-1]:
            a1[m+n-1] = a1[m-1]
            m -= 1
        else:
            a1[m+n-1] = a2[n-1]
            n -= 1

    # we fill a1 with remaining a2 elements if there are any
    if n > 0:
        a1[:n] = a2[:n]


if __name__ == "__main__":
    a1 = [1, 2, 3, 0, 0, 0]
    a2 = [2, 5, 6]
    m, n = 3, 3
    merge_sorted_arrays(a1, m, a2, n)
    print(a1)
