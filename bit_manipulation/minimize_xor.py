"""
leetcode 2429: minimize XOR

Given two positive integers A and B, find the positive integer x such that:

* x has the same number of set bits as B
* the value of x XOR A is minimal
"""


def min_xor(A, B):
    """
    If A has 5 bits set, the minimum possible x is 11111.

    If 11111 >= A, then we return this value of x.

    If 11111 < A, the situation is more complicated:

    A: 10100101
    x: 00011111

    We iteratively move the most significant bit of x to the position of the
    most significant bit of A until x >= A.


    after step 1
    A: 10100101
    x: 10001111

    after step 2 (we're done)
    A: 10100101
    x: 10100111
    """
    nbits = bin(B).count("1")
    x = (1 << nbits) - 1

    # Index of the most significant bit in A or x.
    msb_a = 30
    msb_x = nbits - 1

    # Until x >= A or there's not more bits in x to shift.
    while x < A and msb_x >= 0:

        # Find the most significant bit of A.
        while (1 << msb_a) & A == 0:
            msb_a -= 1

        # Calculate the new value of x after shifting its most significant bit.
        x += (1 << msb_a) - (1 << msb_x)

        msb_a -= 1
        msb_x -= 1

    return x


def test1():
    assert min_xor(3, 5) == 3
    print("test 1 successful")


def test2():
    assert min_xor(1, 12) == 3
    print("test 2 successful")


def test3():
    assert min_xor(64, 40) == 65
    print("test 3 successful")


def test4():
    assert min_xor(31, 31) == 31
    print("test 4 successful")


def main():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    main()
