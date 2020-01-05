# leetcode 38 count and say
# from an integer n return the corresponding sequence such that:
# n = 1: '1'
# n = 2: '11'
# n = 3: '21'
# n = 4: '1211'
# n = 5: '111221'
# etc

from itertools import groupby


def say(s):
    """
    Helper function which converts a sequence of identical
    integers into its 'said' version. For example, '111' is
    converted into '31'.

    :param str s: sequence of integers to convert
    :return str: 'said' version of input
    """
    return str(len(s) * 10 + int(s[0]))


def count_and_say(n):
    """
    Return the nth term of the 'count and say' series.

    :param int n: number of the series' term to return
    :return str: nth term of the 'count and say series'
    """
    # answer for the first term
    answer = '1'

    # we iterate over subsequent terms
    for i in range(1, n):
        # sequence to iterate over is the previous term
        sequence = answer
        # we regenerate the nth term
        answer = ''
        # boundary for the current sequence of identical integers
        low = 0
        # position in the sequence
        index = 1
        # we iterate over the sequence...
        while index < len(sequence):
            # ...and identify every sequence of identical integers
            if sequence[index] != sequence[index - 1]:
                answer += say(sequence[low:index])
                low = index
            index += 1

        # we 'say' the last sequence of identical integers
        answer += say(sequence[low:])

    return answer


def count_and_say2(n):
    """
    Short version using itertools.groupby.

    :param int n: number of the series' term to return
    :return str: nth term of the 'count and say series'
    """
    answer = '1'
    for _ in range(n - 1):
        answer = ''.join(str(len(list(group))) + digit for digit, group in
                groupby(answer))
    return answer


if __name__ == '__main__':
    solutions = [
        '',
        '1',
        '11',
        '21',
        '1211',
        '111221',
        '312211',
        '13112221',
        '1113213211'
    ]
    for i in range(1, len(solutions)):
        found = count_and_say(i)
        expected = solutions[i]
        assert found == expected, (found, expected)
