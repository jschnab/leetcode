# leetcode challenge 494
# given a list of integers and a target integer, find the number of
# ways to obtain the target by adding all integers of the list with
# either a + or - symbol
# for inputs [1,1,1,1,1] and 3, the expected result is 5

def fun(nums, i, sum_, target):
    """Recursively find the number of ways to obtain target with
list of integers nums."""
    # if we reach the end of the list, we check if the sum is equal
    # to the target and add 1 to the answer if it is
    global answer

    if i == len(nums):
        if sum_ == target:
            answer += 1

    # else recursively go through list with either subtraction or addition
    else:
        fun(nums, i+1, sum_+nums[i], target)
        fun(nums, i+1, sum_-nums[i], target)

def target_sum(nums, target):
    global answer
    answer = 0
    fun(nums, 0, 0, target)
    return answer
