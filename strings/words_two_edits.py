"""
leetcode 2452: words within two edits of dictionary

We are given two string arrays, 'queries' and 'dictionary'. All words in each
array comprise of lowercase English letters and have the same length.

In one edit, we can take a word from queries and change any letter in it to any
other letter. Find all words from queries that, after a maximum of two edits,
equal some word from dictionary.

Return a list of all words from queries that match with some word from
dictionary after a maximum of two edits. Return the words in the same order
they appear in queries.
"""


def two_edits(queries, dictionary):
    result = []
    for q in queries:
        match = False
        for d in dictionary:
            if len(q) == len(d) and sum(i != j for i, j in zip(q, d)) <= 2:
                result.append(q)
                match = True
            if match:
                break
    return result


def test1():
    queries = ["word", "note", "ants", "wood"]
    dictionary = ["wood", "joke", "moat"]
    expected = ["word", "note", "wood"]
    assert two_edits(queries, dictionary) == expected
    print("test 1 successful")


def test2():
    queries = ["yes"]
    dictionary = ["not"]
    assert two_edits(queries, dictionary) == []
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
