# leetcode 724
# find the index of the array element such that the sum of elements to
# the left and the sum of elements to the right are equal
# (excluding the pivot)

def pivot_index(array):
    """Return index of pivot element. Sum of elements to the right
and sum of elements to the left of the pivot are equal.
    [1, 7, 3, 6, 5, 6] returns 3"""
    left = 0
    right = sum(array)
    for i in range(len(array)):
        right -= array[i]
        if left == right:
            return i
        left += array[i]
    return -1
