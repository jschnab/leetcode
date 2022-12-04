"""
leetcode 2437: number of valid clock times

We are given a string of length 5 named 'time', representing the current time
on a digital clock in the format hh:mm. The earliest possible time is 00:00 and
the latest possible time is 23:59.

In the string time, the digits represented by the ? symbol are unknown, and
must be replaced by a digit.

Return an integer answer, the number of valid clock times that can be created
by replacing every ? with a digit.
"""
import re


def valid_times(time):
    time = time.replace("?", ".")
    return sum(
        re.fullmatch(time, f"{hour:02}:{minute:02}") is not None
        for hour in range(24) for minute in range(60)
    )


def test1():
    assert valid_times("?5:00") == 2
    print("test 1 successful")


def test2():
    assert valid_times("0?:0?") == 100
    print("test 2 successful")


def test3():
    assert valid_times("??:??") == 1440
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
