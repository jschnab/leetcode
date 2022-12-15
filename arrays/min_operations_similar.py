"""
leetcode 2449: minimum number of operations to make arrays similar

We are given two positive integer arrays nums and target, of the same length.

In one operation, we can choose any two distinct indices i and j where
0 <= i, j < nums.length and:

* set nums[i] = nums[i] + 2
* set nums[j] = nums[j] - 2

Two arrays are considered to be similar if the frequency of each element in the
same.

Return the minimum number of operations required to make nums similar to
target. We assume that nums can always be similar to target.
"""


def make_similar(nums, target):
    """
    Operations can add or subtract 2 to elements, so we have to process odd and
    even numbers separately (an odd number will not be equal to an even number,
    and vice versa).

    We sort odd and even numbers separately, and find the difference between
    the sorted arrays of nums and target. We finally divide by 4 because each
    operation can add (or subtract) 2 to 2 numbers.
    """
    odd_nums = sorted([n for n in nums if n & 1])
    even_nums = sorted([n for n in nums if not n & 1])
    odd_target = sorted([t for t in target if t & 1])
    even_target = sorted([t for t in target if not t & 1])
    odd_diff = sum(abs(a - b) for a, b in zip(odd_nums, odd_target))
    even_diff = sum(abs(a - b) for a, b in zip(even_nums, even_target))
    return (odd_diff + even_diff) // 4


def test1():
    assert make_similar([8, 12, 6], [2, 14, 10]) == 2
    print("test 1 successful")


def test2():
    assert make_similar([1, 2, 5], [4, 1, 3]) == 1
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
