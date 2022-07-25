"""
leetcode 2260: Minimum consecutive cards to pick up.

You are given an integer array A where A[i] represents the value of the ith
card. A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a
pair of matching cards among the picked cards. If it is impossible to have
matching cards return -1.
"""


def n_cards(A):
    val_to_idx = {}
    result = -1
    for i, c in enumerate(A):
        if c in val_to_idx:
            if result != -1:
                result = min(result, i - val_to_idx[c] + 1)
            else:
                result = i - val_to_idx[c] + 1
        val_to_idx[c] = i
    return result


def test1():
    assert n_cards([3, 4, 2, 3, 4, 7]) == 4
    print("test 1 successful")


def test2():
    assert n_cards([1, 0, 5, 3]) == -1
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
