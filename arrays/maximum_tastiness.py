"""
leetcode 2517: maximum tastiness of candy basket

We are given an array of positive integers price where price[i] is the price of
the ith candy and a positive integer k.

The store sells baskets of k distinct candies. The tastiness of a candy basket
is the smallest absolute difference of the prices of any two candies in the
basket.

Return the maximum tastiness of a candy basket.
"""


def max_tasty(price, k):
    price.sort()
    lo = 0
    hi = price[-1] - price[0]
    while lo < hi:
        mid = (lo + hi + 1) // 2
        cnt = 1
        j = 0
        for i in range(1, len(price)):
            if price[i] - price[j] >= mid:
                cnt += 1
                j = i
        if cnt >= k:
            lo = mid
        else:
            hi = mid - 1
    return lo


def test1():
    assert max_tasty([13, 5, 1, 8, 21, 2], 3) == 8
    print("test 1 successful")


def test2():
    assert max_tasty([1, 3, 1], 2) == 2
    print("test 2 successful")


def test3():
    assert max_tasty([7, 7, 7, 7], 2) == 0
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
