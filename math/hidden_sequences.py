"""
We are given an array of n integers that represent differences between
consecutive elements of a hypothetical sequence of n + 1 integers.

We are also given two integers that represent the minimum and maximum values
of the hypothetical sequence (inclusive).

We want to determine the number of hypothetical sequences that exist.
"""


def hidden_sequences(diff, low, high):
    """
    We calculate the relative range of integers covered by ``diff``, and the
    range covered by ``low`` and ``high``. We then calculate how many
    sequences with range defined by ``diff`` can fit between ``low`` and
    ``high`.

    Time complexity is linear and space complexity is constant.

    :param list[int] diff: List of differences.
    :param int low: Low boundary for the hidden sequence.
    :param int high: High boundary for the hidden sequence.
    :returns (int): Number of hidden sequences.
    """
    # range covered by diff is relative so we start at 0
    mini = maxi = i = 0
    for j in diff:
        i += j
        mini = min(mini, i)
        maxi = max(maxi, i)
    # number of hidden sequences is at least 0
    return max(0, high - low - (maxi - mini) + 1)


def test1():
    assert hidden_sequences([1, -3, 4], 1, 6) == 2
    print("test 1 successful")


def main():
    test1()


if __name__ == "__main__":
    main()
