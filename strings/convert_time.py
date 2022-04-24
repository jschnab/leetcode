"""
We have two strings A and B that represent 24h times, formatted as HH:MM,
such as A is earlier than B.

In one operation we can increase time A by 1, 5, 15, or 60 minutes. We can
perform these operations any number of times.

Calculate the minimum number of operations needed to convert A to B.
"""


def convert_times(A, B):
    """
    We determine the number of minutes between A and B, then determine how
    many times we can apply operations starting from the largest (60 minutes)
    down to the smallest (1 minute).
    """
    hh, mm = map(int, A.split(":"))
    A_minutes = hh * 60 + mm
    hh, mm = map(int, B.split(":"))
    B_minutes = hh * 60 + mm
    diff = B_minutes - A_minutes
    result = 0
    for t in (60, 15, 5):
        result += diff // t
        diff %= t
    return result + diff


def test1():
    assert convert_times("02:30", "04:35") == 3
    print("test 1 successful")


def test2():
    assert convert_times("11:00", "11:01") == 1
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
