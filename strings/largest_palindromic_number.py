"""
leetcode 2384: largest palindromic number

We are given a string S consisting of digits only.

Return the largest palindromic integer (formatted as a string) that can be
formed using digits taken from S. It should not contain leading zeroes.

Notes:

* we do not need to use all the digits of S, but we must at least use one.
* the digits can be re-ordered.
"""
import heapq
from collections import Counter


def palindrome(S):
    """
    We count digits and build half of the final palindromic string, which we
    append with a reverse of itself before returning.

    We may have to add a single digit in the center of final string, so we
    keep track of it separately.

    If the count of digits is odd and at least 3, we can use an even count of
    digits in the palindrome and we are left with one remaining digit. Using a
    dictionary makes keeping track of this lonely digit, so we use a heap.
    """
    nums = [int(i) for i in S]
    heap = [(-d, c) for d, c in Counter(nums).items()]
    heapq.heapify(heap)
    if heap[0][0] == 0:
        return "0"
    result = []
    single = -1
    while heap:
        digit, count = heapq.heappop(heap)

        # if count is even
        if not count & 1:
            # make sure we don't have leading zero
            if result != [] or digit != 0:
                result.extend([str(-digit)] * (count // 2))

        # if count is odd but greater than 2, we can use an even number of
        # digits and keep the last one for later
        elif count > 2:
            # make sure we don't have leading zero
            if result != [] or digit != 0:
                result.extend([str(-digit)] * ((count - 1) // 2))
                heapq.heappush(heap, (digit, 1))

        # keep the single digit with the highest value, to put in the center of
        # the palindrome
        elif -digit > single:
            single = -digit

    if single != -1:
        return "".join(result + [str(single)] + result[::-1])
    return "".join(result + result[::-1])


def test1():
    assert palindrome("444947137") == "7449447"
    print("test 1 successful")


def test2():
    assert palindrome("00009") == "9"
    print("test 2 successful")


def test3():
    assert palindrome("00099") == "90009"
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
