"""
leetcode 2243: Calculate digit sum of a string.

Given a string S consisting of digits and an integer k, process and return S
after all rounds of the following procedure:

* a round can be completed if the length of S is greater than k
* divide S into consecutive groups of size k
* replace each group with a string representing the sum of its digits
* merge consecutive groups together to form a new string
"""


def digit_sum(S, k):
    while len(S) > k:
        groups = [S[i:i+k] for i in range(0, len(S), k)]
        replaced = [str(sum(map(int, list(g)))) for g in groups]
        S = "".join(replaced)
    return S


def test1():
    assert digit_sum("11111222223", 3) == "135"
    print("test 1 successful")


def test2():
    assert digit_sum("00000000", 3) == "000"
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
