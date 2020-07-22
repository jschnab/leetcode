# leetcode challenge 560: subarray sum equals k
# given an array of integers and an integer k, we need to find the total
# number of continuous subarrays whose sum equals k
# input: [1,1,1], k = 2
# output: 2

def subarray_sum_brute(nums, k):
    """
    Brute force solution, check every subarray and make its sum.
    Time complexity: O(n^2)
    Space complexity: O(n)

    :param list[int] nums:
    :params int k:
    :return int:
    """
    answer = 0
    length = len(nums)
    for i in range(length):
        sum_ = 0
        for j in range(i, length):
            sum_ += nums[j]
            if sum_ == k:
                answer += 1
    return answer


def subarray_sum_linear(nums, k):
    """
    More scalable solution, make the cumulative sum of the array
    and check how many values in the cumulative sum are separated by k.
    Time complexity: O(n)
    Space complexity: O(n)

    :param list[int] nums:
    :params int k:
    :return int:
    """
    answer = 0
    sum_ = 0
    count = {0: 1}
    for n in nums:
        sum_ += n
        answer += count.get(sum_ - k, 0)
        count[sum_] = count.get(sum_, 0) + 1
    return answer


def test1():
    assert subarray_sum_linear([1,1,1], 2) == 2
    print("test 1 successful")


def test2():
    assert subarray_sum_brute([1,1,1], 2) == 2
    print("test 2 successful")


if __name__ == "__main__":
    test1()
    test2()
