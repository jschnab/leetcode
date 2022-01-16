"""
You start with integer 1 and want to reach a target integer.

In one move, you can either increment your value by 1 or multiply it by 2.

You may use the increment operation as many times as you want, but the
number of multiplications is limited.

Given two integers 'target' and 'max_multiply', we want to determine the
number of moves necessary to reach 'target' when starting from 1.
"""


def min_moves(target, max_multiply):
    moves = 0
    # we start from target and reach 1
    while target > 1 and max_multiply:
        # combine increment and multiply in a single operation
        moves += 1 + target % 2
        max_multiply -= 1
        target >>= 1
    # once we either exhausted the number of multiplication, the number of
    # increment operations is the difference between target and 1
    return target - 1 + moves
