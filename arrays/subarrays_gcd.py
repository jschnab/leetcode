"""
leetcode 2447: number of subarrays with GCD equal to K

Given an integer array nums and an integer k, return the number of subarrays of
nums where the greatest common divisor of the subarray's elements is k.

A subarray is a contiguous non-empty sequence of elements within an array.

The greatest common divisor of an array is the largest integer that evently
divides all the array elements.
"""
import math


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def subarray_gcd(nums, k):
    """
    We simply perform a brute-force algorithm: we iterate over all possible
    subarray of nums and count how many subarrays have their gcd equal to k.
    """
    result = 0
    for i in range(len(nums)):
        cur = nums[i]
        for j in range(i, len(nums)):
            cur = gcd(cur, nums[j])
            if cur == k:
                result += 1
    return result


def test1():
    assert subarray_gcd([9, 3, 1, 2, 6, 3], 3) == 4
    print("test 1 successful")


def test2():
    assert subarray_gcd([4], 7) == 0
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
