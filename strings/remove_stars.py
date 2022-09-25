"""
leetcode 2390: removing stars from a string

We are given a string S, which contains '*' characters (stars).

In one operation, we can do both following actions:

* choose a star in S
* remove the closest non-start characters to its left, as well as remove the
  star itself

Return S after all stars have been removed.

Notes:

* the input is given such that the operation is always possible to complete, if
initiated
* the resulting string will always be unique
"""


def remove_stars(S):
    j = 0
    result = [None] * len(S)
    for i in range(len(S)):
        if S[i] != "*":
            result[j] = S[i]
            j += 1
        else:
            j -= 1
    return "".join(result[:j])


def test1():
    assert remove_stars("leet**cod*e") == "lecoe"
    print("test 1 successful")


def test2():
    assert remove_stars("erase*****") == ""
    print("test 2 successful")


def test3():
    assert remove_stars("hello") == "hello"
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
