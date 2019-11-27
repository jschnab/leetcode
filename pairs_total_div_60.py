# leetcode problem 1013
# given a list of integers, find the number of pairs which sum is
# divisible by 60

def pairs_div_60(int_list):
    """Determine the number of pairs which sum is divisible by 60
    [30, 20, 150, 100, 40] returns 3
    [60, 60, 60] returns 3"""

    counts = [0] * 61
    answer = 0
    for i in int_list:
        # we have to make sure the pair (60, 60) is counted
        answer += counts[(60 - i % 60) % 60]
        counts[i % 60] += 1
    return answer
