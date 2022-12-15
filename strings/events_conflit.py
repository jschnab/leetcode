"""
leetcode 2446: determine if two events have a conflict

We are given two arrays of strings that represent two inclusive events that
happened on the same day, event1 and event2, where:

* event1 = [start_time1, end_time1]
* event2 = [start_time2, end_time2]

Event times are valid 24 hours format in the form of HH:MM.

A conflict happens when two events have some non-empty intersection (i.e. some
moment is common to both events).

Return True if there is a conflict between two events. Otherwise return False.
"""


def conflict(event1, event2):
    """
    One simple way would be to convert both events times in minutes, then check
    for their overlap.

    However, the given format allows for direct lexicographical comparison of
    the strings.
    """
    if event1[0] < event2[0]:
        return event1[1] >= event2[0]
    return event2[1] >= event1[0]


def test1():
    event1 = ["01:15", "02:00"]
    event2 = ["02:00", "03:00"]
    assert conflict(event1, event2) is True
    print("test 1 successful")


def test2():
    event1 = ["01:00", "02:00"]
    event2 = ["01:20", "03:00"]
    assert conflict(event1, event2) is True
    print("test 2 successful")


def test3():
    event1 = ["10:00", "11:00"]
    event2 = ["14:00", "15:00"]
    assert conflict(event1, event2) is False
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
