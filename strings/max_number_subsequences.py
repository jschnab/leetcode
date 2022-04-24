"""
leetcode 2207: Maximize number of subsequences in a string.

We are given a string S and another string of length 2 P (the pattern).
Both S and P only consists of lowercase english letters.

We can add either P[0] or P[1] at any index in S exactly once (including at
the beginning and the end).

Return the maximum number of times P can occur as a subsequence of modified S.

A subsequence is a string that can be derived from another string by deleting
some or no characters without changing the order of the remaining characters.
"""


class MyString:
    """
    This class allows to iterate through the modified string without having
    to generate it.
    """

    def __init__(self, s, c, i):
        """
        :param str s: Original string.
        :param str c: Character to add to the original string.
        :param int i: Index where to add the character in the original string.
        """
        self.s = s
        self.c = c
        self.i = i

    def __len__(self):
        return len(self.s) + 1

    def __str__(self):
        return "".join(c for c in self)

    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.start, index.stop, index.step
            return str(self)[start:stop:step]

        if index < self.i:
            return self.s[index]

        if index == self.i:
            return self.c

        return self.s[index - 1]


def ncs_memo(x, y, verbose=False):
    """
    Number of common subsequences between two strings.

    Bottom-up dynamic programming.

    :param str x: First string.
    :param str y: Second string.
    :returns (int): Number of common subsequences between the strings.
    """
    # memoization grid
    memo = [[0 for _ in range(len(y)+1)] for _ in range(len(x)+1)]

    # where column number is the length of y, we found a subsequence
    # so the score is 1
    for i in range(len(x)+1):
        memo[i][len(y)] = 1

    for i in range(len(x)-1, -1, -1):
        for j in range(len(y)-1, -1, -1):
            if x[i] == y[j]:
                memo[i][j] += memo[i+1][j+1]
            memo[i][j] += memo[i+1][j]

    if verbose:
        for line in memo:
            print(line)

    return memo[0][0]


def ncs_recur(x, y, i, j):
    """
    Number of common subsequences between two strings.

    Top-down recursive approach, no memoization.

    To use this function, call it with i = j = 0.

    :param str x: First string.
    :param str y: Second string.
    :param int i: Index of the first string.
    :param int j: Index of the second string.
    :returns (int): Number of common subsequences between the strings.
    """
    # if we reach the end of the two strings, we found a common subsequence
    if i == len(x) and j == len(y):
        return 1

    # else if we reach the end of the first string only, no common subsequence
    # was found
    if i == len(x):
        return 0

    count = 0

    # if we have matching characters, recurse on substrings
    if j < len(y) and x[i] == y[j]:
        count += ncs_recur(x, y, i + 1, j + 1)

    # regardless of characters matches, we recurse on a substring of x because
    # a character match has two outcomes: being counted or not (later
    # characters of may match the same character of y)
    count += ncs_recur(x, y, i + 1, j)

    return count


def max_subsequence_count1(S, T):
    """
    We notice that since T has only two characters, we can simplify our problem
    by adding T[0] at the beginning of S and T[1] at the end of S.

    After that, we use a dynamic programming approach to count the number of
    common subsequences between modified S and T.

    We use a special string class to avoid generating modified S (it's
    potentially very long).
    """
    # add T[0] at the beginning of S
    s1 = MyString(S, T[0], 0)

    # add T[1] at the end of S
    s2 = MyString(S, T[1], len(S))

    return max(ncs_memo(s1, T), ncs_memo(s2, T))


def max_subsequence_count2(S, T):
    """
    We notice that since T has only two characters, we can simplify our problem
    by adding T[0] at the beginning of S and T[1] at the end of S, so the
    solution is N + max(count(T[0]), count(T[1])) with N the number of
    subsequences of T in S. The second term is due to adding T[0] or T[1] to S.

    To calculate the number of subsequences, we iterate through every character
    in S and count occurrences of T[0] and T[1]. When we encounter T[1], we may
    have a subsequence so we add the count of T[0] to the total count.
    """
    total = 0
    count_0 = 0
    count_1 = 0

    for c in S:
        if c == T[1]:
            total += count_0
            count_1 += 1

        # T[0] may be the same as T[1] so we always check equality
        # we check T[0] after T[1] to avoid counting it twice if they are the
        # same
        if c == T[0]:
            count_0 += 1

    return total + max(count_0, count_1)


def test1():
    assert max_subsequence_count1("abdcdbc", "ac") == 4
    assert max_subsequence_count2("abdcdbc", "ac") == 4
    print("test 1 successful")


def test2():
    assert max_subsequence_count1("aabb", "ab") == 6
    assert max_subsequence_count2("aabb", "ab") == 6
    print("test 2 successful")


def test3():
    assert max_subsequence_count1("x", "jk") == 0
    assert max_subsequence_count2("x", "jk") == 0
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
