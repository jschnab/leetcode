"""
leetcode #2165

Given an integer n, we want to rearrange its digits such that the value of the
rearranged integer is minimized and does not contain leading zeros.

The sign of the rearranged integer should not change.
"""


def rearrange(n):
    """
    We will break down the input integer into its digits, sort them then
    reassemble them into a minimized integer where smallest digits come first.

    Time complexity: O(xlog(x)) since we sort digits, with x the number of
    digits in the input.

    :param int n: Number to minimize.
    :returns (int): Minimized number.
    """
    if n == 0:
        return n

    # we sort digits in different orders depending on the sign of the input
    # so we take a note of the sign
    # we make the input number positive to simplify processing
    if n < 0:
        negative = True
        mult = -1
    else:
        negative = False
        mult = 1
    n *= mult

    # we break down the input number into its digits
    digits = []
    while n != 0:
        digits.append(n % 10)
        n //= 10

    # if the number is positive we put the highest digits at the lowest index
    # so they have the lowest position in the rearranged integer
    if not negative:
        digits.sort(reverse=True)
        i = len(digits) - 1
        # to avoid leading zeros in the rearranged number, we flip the last
        # zero with the last non-zero digit
        while digits[i] == 0:
            i -= 1
            digits[len(digits) - 1], digits[i] = (
                digits[i],
                digits[len(digits) - 1],
            )

    # if the number is negative
    else:
        digits.sort()

    # we reassemble digits into the result
    result = 0
    for i, d in enumerate(digits):
        result += d * 10 ** i
    return result * mult
