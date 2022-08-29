"""
leetcode 2347: best poker hand

We are given an integer array 'ranks' and a character array 'suits'. We have 5
cards where the ith card has rank ranks[i] and suit suits[i].

The following are the types of poker hands we can make from best to worst:

1. "Flush": five cards of the same suit
2. "Three of a kind": three cards of the same rank
3. "Pair" two cards of the same rank
4. "High card": any single card

Return a string representing the best type of poker hand you can make with the
given cards.
"""

from collections import Counter


def best_hand(ranks, suits):
    """
    Time complexity: O(n).
    Space complexity: O(n).
    """
    if max(suits) == min(suits):
        return "Flush"
    maxi = max(Counter(ranks).values())
    if maxi >= 3:
        return "Three of a kind"
    elif maxi == 2:
        return "Pair"
    return "High Card"


def test1():
    ranks = [10, 10, 2, 12, 9]
    suits = ["a", "b", "c", "d"]
    assert best_hand(ranks, suits) == "Pair"
    print("test 1 successful")


def test2():
    ranks = [13, 2, 3, 1, 9]
    suits = ["a", "a", "a", "a", "a"]
    assert best_hand(ranks, suits) == "Flush"
    print("test 2 successful")


def test3():
    ranks = [4, 4, 2, 4, 4]
    suits = ["d", "a", "a", "b", "c"]
    assert best_hand(ranks, suits) == "Three of a kind"
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
