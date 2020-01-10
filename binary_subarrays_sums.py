# leetcode 930
# calculate the number of subarrays with elements sum equal to a given number S
# array = [1,0,1,0,1] and S = 2 returns 4

def bin_subarray_sum(array, S):
    # list to store sum of to A[i]
    L = [0]
    for x in array:
        L.append(L[-1] + x)

    counter = {}
    answer = 0

    for x in L:
        answer += counter.get(x - S, 0)
        counter[x] = counter.get(x, 0) + 1

    return answer
