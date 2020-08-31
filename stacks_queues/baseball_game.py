# leetcode challenge 682: baseball game
# given a list of strings representing baseball round
# each element can be:
# integer: number of points gained in this round
# +: points gained in this round are the sum of the last two rounds
# D: points gained in this round are double of last round
# C: remove the last round points
#
# return the sum of round points
# input: ["5", "2", "C", "D", "+"]


def count_points(operations):
    """
    Count the points of rounds of a baseball game.

    Time complexity: O(n) we iterate through operations and stack operations
                     all take O(1) in amortized complexity
    Space complexity: O(n) we store operations on a stack

    :param list[str] operations: list of operations to count round points
    :returns: int - sum of points
    """
    stack = []
    length = 0
    for op in operations:
        if op == "C":  # cancel last points
            if length >= 1:
                stack.pop()
                length -= 1
        elif op == "D":
            if length >= 1:
                stack.append(2 * stack[-1])
                length += 1
        elif op == "+":
            if length >= 2:
                stack.append(stack[-1] + stack[-2])
                length += 1
        else:
            stack.append(int(op))
            length += 1
    return sum(stack)
