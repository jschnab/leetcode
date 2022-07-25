"""
leetcode 2271: Maximum white tiles covered by a carpet.

You are given a 2D integer array 'tiles' where tiles[i] = [l, r] represents
that every tile j in the range l <= j <= r is colored white.

You are also given an integer 'length', the length of a single carpet that can
be placed anywhere.

Return the maximum number of white tiles that can be covered by the carpet.
"""


def max_tiles(tiles, length):
    """
    Returns the maximum number of tiles that can be covered by the carpet.

    :param list(list(int)) tiles: Tiles.
    :param int length: Length of the carpet.
    """
    tiles.sort()
    cum_len = [0]
    ends = []
    for l, r in tiles:
        cum_len.append(cum_len[-1] + r - l + 1)
        ends.append(r)
    result = 0
    j = 0
    for i in range(len(ends)):
        r = min(ends[-1], tiles[i][0] + length - 1)
        while j < len(ends) and ends[j] < r:
            j += 1
        if tiles[j][0] <= r:  # carpet reaches jth range
            result = max(result, cum_len[j + 1] - cum_len[i] - (ends[j] - r))
        else:
            result = max(result, cum_len[j] - cum_len[i])
    return result


def test1():
    tiles = [[1, 5], [10, 11], [12, 18], [20, 25], [30, 32]]
    length = 10
    assert max_tiles(tiles, length) == 9
    print("test 1 successful")


def test2():
    tiles = [[10, 11], [1, 1]]
    length = 2
    assert max_tiles(tiles, length) == 2
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
