"""
leetcode 2511: maximum enemy forts that can be captured

We are given an integer array 'forts' of length n representing the positions of
several forts. forts[i] can be -1, 0, or 1 where:

* -1 means there is no fort at the ith position
* 0 means there is an enemy fort
* 1 indicates the fort is under our command

We have decided to move our army from one of our forts at position i to an
empty position j such that:

* 0 <= i, j <= n - 1
* the army travels over enemy forts only
  for all k where min(i, j) < k < max(i, j) forts[k] == 0

While moving the army, all the enemy forts that come in the way are captured.

Return the maximum number of enemy forts that can be captured. In case it is
impossible to move the army, or we do not have any forts under our command,
return 0.
"""


def capture(forts):
    """
    We count how many adjacent enemy forts are between empty and friendly
    positions.

    We iterate once but we still need to account movement in both left-to-right
    and right-to-left directions, so we need to keep track of whether we have
    previously encountered a friendly fort or empty fort.
    """
    maxi = 0
    count = 0
    seen_friend = False
    seen_empty = False
    for fo in forts:
        if fo == 0:     # enemy fort
            count += 1
        elif fo == -1:  # no fort
            if seen_friend:
                maxi = max(maxi, count)
                seen_friend = False
            seen_empty = True
            count = 0  # move over enemy forts only
        else:          # fort under command
            if seen_empty:
                maxi = max(maxi, count)
                seen_empty = False
            seen_friend = True
            count = 0  # move over enemy forts only
    return maxi


def capture2(forts):
    maxi = 0
    i = 0
    for j in range(len(forts)):
        if forts[j] != 0:
            if forts[i] == -forts[j]:
                maxi = max(maxi, j - i - 1)
            i = j
    return maxi


def test1():
    assert capture([1, 0, 0, -1, 0, 0, 0, 0, 1]) == 4
    assert capture2([1, 0, 0, -1, 0, 0, 0, 0, 1]) == 4
    print("test 1 successful")


def test2():
    assert capture([0, 0, 1, -1]) == 0
    assert capture2([1, 0, 0, -1, 0, 0, 0, 0, 1]) == 4
    print("test 2 successful")


def test3():
    assert capture([1, 0, 0, 1, 0, 0, -1]) == 2
    assert capture2([1, 0, 0, 1, 0, 0, 0, 0, -1]) == 4
    print("test 3 successful")


def test4():
    assert capture([-1, 0, 0, -1, 0, 0, 1]) == 2
    assert capture2([-1, 0, 0, -1, 0, 0, 0, 0, 1]) == 4
    print("test 4 successful")


def test5():
    assert capture([0, -1, 0, 0, -1, 0, 0, 1]) == 2
    assert capture2([0, -1, 0, 0, -1, 0, 0, 0, 0, 1]) == 4
    print("test 5 successful")




def main():
    test1()
    test2()
    test3()
    test4()
    test5()


if __name__ == "__main__":
    main()
