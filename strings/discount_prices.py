"""
leetcode 2288: apply discount to prices.

A sentence is a string of single-space-separated words where each word can
contain digits, lowercase letters, and the dollar sign. A word represents a
price if it is a sequence of digits preceded by a dollar sign. For example,
100, $, and $1e5 are not prices.

We are given a string S representing a sentence and in integer d representing a
discount (in percent). For each word representing a price, apply a discount one
the price and update the word in the sentence. All updated prices should be
represented with two decimal places.

Return the modified sentence as a string.
"""


def discount_prices(S, d):
    words = S.split()
    for i, w in enumerate(words):
        if w.startswith("$") and w[1:].isnumeric():
            words[i] = f"${float(w[1:]) * (1 - d / 100):.2f}"
    return " ".join(words)


def test1():
    S = "there are $1 $2 and 5$ candies in the shop"
    expected = "there are $0.50 $1.00 and 5$ candies in the shop"
    assert discount_prices(S, 50) == expected
    print("test 1 successful")


def test2():
    S = "1 2 $3 4 $5 $6 7 8$ $9 $10$"
    expected = "1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$"
    assert discount_prices(S, 100) == expected
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
