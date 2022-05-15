"""
leetcode 2240: Number of ways to buy pens and pencils.

We are given an integer T indicating an amount of money, and integer X
indicating the price of a pen, and an integer Y indicating the price of a
pencil. We can spend part or all of T to buy 0 or more pens and/or pencils.

We calculate the number of distinct ways we can spend our money on pens
and pencils.
"""


def buy(T, X, Y):
    result = 0
    for i in range(T // X + 1):  # +1 if you don't buy pens
        remain = T - i * X  # remaining money after buying pens
        # even if we have 0 money left, not buying pencils is an option
        if remain >= 0:
            result += remain // Y + 1  # +1 if you don't buy pencils
    return result


def test1():
    assert buy(20, 10, 5) == 9
    print("test 1 successful")


def test2():
    assert buy(5, 10, 10) == 1  # 1 option: buy 0 pens and 0 pencils
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
