# leetcode challenge 739: daily temperatures
# given a list of daily temperatures, return a list such that for each day
# in the input, tells you how many days followed until a warmer temperature
# if there is no such day put '0'


def daily_temperatures(T):
    """
    Return a list of the number of days until a warmer temperature,
    for each day in the input list.

    Time complexity: O(n) we iterate through the list once
    Space complexity: O(n) we store a list with the same size as the input

    :param list[str] T: list of temperatures
    :returns: list[int] - list of number of days until a warmer temperature
    """
    stack = []
    result = [0] * len(T)
    for i, temp in enumerate(T):
        while stack and stack[-1][1] < temp:
            j, prev_temp = stack.pop()
            result[j] = i - j
        stack.append((i, temp))
    return result


def test1():
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    assert daily_temperatures(T) == [1, 1, 4, 2, 1, 1, 0, 0]
    print("test 1 successful")


def main():
    test1()


if __name__ == "__main__":
    main()
