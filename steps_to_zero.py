# leetcode problem 1342: number of steps to reduce number to 0
# given a non-negative integer, return the number of steps to reduce it
# to zero.
# if the current number is even, divide by 2, if it is odd subtract 1 from it

def steps_to_zero(n):
    steps = 0
    while n != 0:
        if n & 1:
            n -= 1
        else:
            n /= 2
        steps += 1
    return steps
