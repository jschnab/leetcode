"""
leetcode 2571: minimum operations to reduce and integer to 0.

We are given a positive integer n, we can do the following operation any number
of times: add or subtract a power of 2 from n.

Return the minimum number of operations to make n equal to 0.
"""

def minop(n):
    # If there are x set bits, we would need to subtract a power of 2 x times
    # to get to 0.
    nbits = bin(n).count("1")

    # We try to reduce sequences of set bits to a single 1 by judiciously
    # adding a power of 2, and count how many times we dot it.
    count = 0
    begin = None  # Marks the beginning of a sequence of set bits.
    for i in range(19):  # n < 2^19 (including after adding power of 2)
        if n & (1 << i):
            if begin is None:
                begin = i
        else:
            if begin is not None:
                # If we reduce a sequence it's one operation, and if we don't
                # reduce we still have to perform one operation to set the last
                # bit to zero, so we always increment count.
                count += 1
                if i - begin >= 2:
                    n += 1 << begin
                    begin = i
                else:
                    begin = None
    return min(nbits, count)


def minop2(n):
    count = 0
    # If we add 2^14 to n, there can only be two additional bits set, at most.
    # Reducing them by addition or subtraction has the same number of
    # operations, so we just stop iterating at 14 and count remaining bits.
    for i in range(14):
        add = n + (1 << i)
        if bin(add).count("1") < bin(n).count("1"):
            n = add
            count += 1
    return count + bin(n).count("1")


def test1():
    assert minop(39) == 3
    assert minop2(39) == 3
    print("test 1 successful")


def test2():
    assert minop(54) == 3
    assert minop2(54) == 3
    print("test 2 successful")


def test3():
    assert minop(64) == 1
    assert minop2(64) == 1
    print("test 3 successful")


if __name__ == "__main__":
    test1()
    test2()
    test3()
