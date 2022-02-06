"""
A store is selling candies at a discount. For two candies bought, we can buy a
third candy if the price of the third candy is less than the minimum price of
the two candies bought.

Given an array of candies that represent the cost of candies, return the
minimum price of buying all candies.
"""


def buy_candies(prices):
    """
    We sort prices and we buy all candies starting at the most expensive one.
    We skip every one of three candies because we can get this one for free.

    :param list[int] prices: Price of candies.
    :returns (int): Minimum price of buying all candies, including discount.
    """
    prices.sort(reverse=True)
    total = 0
    for i in range(len(prices)):
        if i % 3 != 2:
            total += prices[i]
    return total


def test1():
    assert buy_candies([1, 2, 3]) == 5
    print("test 1 successful")


def test2():
    assert buy_candies([5, 5]) == 10
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
