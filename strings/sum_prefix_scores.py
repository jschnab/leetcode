"""
leetcode 2416: We are given an array W (words) of size n consisting of
non-empty strings.

We defined the score of a string w as the number of strings W[i] such that w is
a prefix of W[i].

For example, if W = ["a", "ab", "abc", "cab"], then the score of "ab" is 2,
since "ab" is a prefix of both "ab" and "abc".

Return an array of size n where the value at index i is the sum of scores of
every non-empty prefix of W[i].

Note that a string is considered as a prefix of itself.
"""
from collections import defaultdict


def scores(W):
    """
    Time complexity: O(n * m) where n is the number of words and m is the
    length of the longest word.
    Space complexity: O(n^2).
    """
    result = [0] * len(W)
    counter = defaultdict(int)
    for word in W:
        for i in range(1, len(word) + 1):
            counter[word[:i]] += 1

    for i, word in enumerate(W):
        for j in range(1, len(word) + 1):
            result[i] += counter[word[:j]]

    return result


class Node:
    """
    Trie node.
    """
    def __init__(self):
        self.children = {}
        self.count = 0


class Trie:
    def __init__(self):
        self.start = Node()

    def insert(self, word):
        node = self.start
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
            node.count += 1


def scores_trie(W):
    t = Trie()
    for word in W:
        t.insert(word)

    result = []
    for word in W:
        count = 0
        node = t.start
        for char in word:
            node = node.children[char]
            count += node.count
        result.append(count)

    return result


def test1():
    assert scores(["abc", "ab", "bc", "b"]) == [5, 4, 3, 2]
    assert scores_trie(["abc", "ab", "bc", "b"]) == [5, 4, 3, 2]
    print("test 1 successful")


def test2():
    assert scores(["abcd"]) == [4]
    assert scores_trie(["abcd"]) == [4]
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
