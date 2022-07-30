"""
leetcode 2300: Successful pairs of spells and potions.

We are given two positive integer arrays S and P, representing spells and
potions, with length n and m, respectively. S[i] represents the strength of the
ith spell and P[j] represents the strength of the jth potion.

We are also given an integer k. A spell and potion pair is successful if the
product of their strengths is at least k.

Return the integer array A of length n where A[i] is the number of potions that
will form a successful pair with the ith spell.
"""


def success(spells, potions, k):
    """
    We notice that if the combination of a potion with a spell is successful,
    then all spells stronger than this spell will be successful with this
    potion, so we sort spells and also store their index in the sorted array
    so that we can assemble the solution. We also sort potions.

    First, we find the weakest potion that is successful with the weakest
    spell. All stronger potions will be successful with the weakest spell, so
    at this point we solved the problem for the weakest potion. We store the
    index of the cutoff potion in the variable 'start', so that we do not check
    stronger potions in the future (they will always be successful as we
    iterate through stronger spells).

    Then, we iterate through spells from the weakest to the strongest. The
    number of success is at least that of weaker spells, a number we store in
    the variable 'carry'. We now need to calculate how many more potions are
    successful with this spell, so we iterate through potions from stronger to
    weaker and stop once the combination is not successful anymore. We also
    update 'carry' and 'start' for future iterations.

    Time complexity: O(nlogn + mlogm) where n is the number of spells and m the
    number of potions, because we sort the array of potions and spells.

    Space complexity: O(m), we store the result in an array of size m.
    """
    spells = sorted(
        ((value, index) for index, value in enumerate(spells)),
        key=lambda x: x[0]
    )
    potions.sort()
    result = [0] * len(spells)
    start = len(potions) - 1
    carry = 0

    # We find the weakest potion that is successful with the weakest spell.
    for j, p in enumerate(potions):
        if spells[0][0] * p >= k:
            carry = len(potions) - j
            start = j - 1
            result[spells[0][1]] = carry
            break

    # We iterate over spells and remaining potions.
    for i, (vsp, isp) in enumerate(spells[1:], start=1):
        result[isp] = carry
        j = start
        while j >= 0:
            if vsp * potions[j] < k:
                break
            result[isp] += 1
            carry += 1
            j -= 1
        start = j
    return result


def test1():
    assert success([5, 1, 3], [1, 2, 3, 4, 5], 7) == [4, 0, 3]
    print("test 1 successful")


def test2():
    assert success([3, 1, 2], [8, 5, 8], 16) == [2, 0, 2]
    print("test 2 successful")


def test3():
    assert success([15, 8, 19], [38, 36, 23], 328) == [3, 0, 3]
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
