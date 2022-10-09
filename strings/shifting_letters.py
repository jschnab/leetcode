"""
leetcode 2381: shifting letters

We are given a string S of lowercase English letters and a 2D integer array
shifts where shifts[i] = (start, end, direction). For every i, shift the
characters in S from the index start to the index end (inclusive) forward if
direction = 1, of shift the characters backward if direction = 0.

Shifting a character forward means replacing it with the next letter in the
alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a
character backward means replacing it with the previous letter in the alphabet
(wrapping around so that 'a' becomes 'z').

Return the final string after all such shifts to S are applied.
"""


def shifting(S, shifts):
    """
    To avoid iterating through all indexes of the shift intervals, we store the
    shifts at the beginning and end of each interval. When we shift letters, we
    accumulate shifts.

    Time complexity: O(n) to iterate through shifts then through letters and
    shift them.
    Space complexity: O(n) to store shifts.
    """
    line = [0] * (len(S) + 1)
    for start, end, direction in shifts:
        if direction:
            line[start] += 1
            line[end + 1] -= 1  # indexes are inclusive
        else:
            line[start] -= 1
            line[end + 1] += 1
    result = []
    val = 0
    for i in range(len(S)):
        val += line[i]
        result.append(chr((ord(S[i]) - ord("a") + val) % 26 + ord("a")))
    return "".join(result)


class Fenwick:
    def __init__(self, items):
        self.items = [0] * (len(items) + 1)
        for i, x in enumerate(items):
            self.update_item(i, x)

    def lsb(self, x):
        return x & -x

    def update_item(self, i, x):
        i += 1
        while i < len(self.items):
            self.items[i] += x
            i += self.lsb(i)

    def prefix_sum(self, i):
        i += 1
        s = self.items[0]
        while i > 0:
            s += self.items[i]
            i -= self.lsb(i)
        return s


def shifting_fenwick(S, shifts):
    """
    This time we will store all shifts, so to have better time complexity we
    use a Fenwick tree (aka binary-indexed tree) to calculate shift sums.

    Time complexity: O(nlogn) to iterate through S or shifts items then call
    update_item or prefix_sum methods on the tree, which take O(logn).
    Space complexity: O(n) to store shifts in the tree.
    """
    f = Fenwick([0] * (len(S) + 1))
    for start, end, direction in shifts:
        if direction:
            f.update_item(start, 1)
            f.update_item(end + 1, -1)
        else:
            f.update_item(start, -1)
            f.update_item(end + 1, 1)
    result = []
    for i in range(len(S)):
        result.append(
            chr((ord(S[i]) - ord("a") + f.prefix_sum(i)) % 26 + ord("a"))
        )
    return "".join(result)


def test1():
    S = "abc"
    shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
    assert shifting(S, shifts) == "ace"
    assert shifting_fenwick(S, shifts) == "ace"
    print("test 1 successful")


def test2():
    S = "dztz"
    shifts = [[0, 0, 0], [1, 1, 1]]
    assert shifting(S, shifts) == "catz"
    assert shifting_fenwick(S, shifts) == "catz"
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
