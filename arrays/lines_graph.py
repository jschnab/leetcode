"""
leetcode 2280: Minimum lines to represent line chart.

Given a 2D integer array 'prices' where price[i] = (day, price) indicates the
price of a stock on 'day' is 'price', a line chart is created from the array by
plotting the points on a 2D plane with the x-axis representing the day and the
y-axis representing the price, and connecting adjacent points.

Return the minimum number of lines needed to represent the line chart.
"""


def min_lines(prices):
    """
    Number of lines to draw line chart.

    To avoid rounding errors with floats, we cross-multiply coordinates to find
    out if points are aligned, instead of comparing slopes with a division.

    :param list(list(int)) prices: Price of stock for each day.
    :returns (int): Minimum number of lines to draw the chart.
    """

    def not_same_line(a, b, c):
        """
        Returns False if three points a, b, and c are aligned, else True.

        First element of each point is x, second element is y.

        :param list(list(int)) a: First point.
        :param list(list(int)) b: Second point.
        :param list(list(int)) c: Third point.
        :returns (bool): True if points are not aligned.
        """
        return (b[1] - a[1]) * (c[0] - b[0]) != (b[0] - a[0]) * (c[1] - b[1])

    if len(prices) <= 2:
        return len(prices) - 1

    prices.sort()
    result = 1
    for i in range(2, len(prices)):
        result += not_same_line(prices[i], prices[i - 1], prices[i - 2])
    return result


def test1():
    prices = [[1, 7], [2, 6], [3, 5], [4, 4], [5, 4], [6, 3], [7, 2], [8, 1]]
    assert min_lines(prices) == 3
    print("test 1 successful")


def test2():
    prices = [[3, 4], [1, 2], [7, 8], [2, 3]]
    assert min_lines(prices) == 1
    print("test 2 successful")


def test3():
    assert min_lines([[1, 2], [3, 4]]) == 1
    print("test 3 successful")


def test4():
    prices = [[1, 1], [500000000, 499999999], [1000000000, 999999998]]
    assert min_lines(prices) == 2
    print("test 4 successful")


def main():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    main()
