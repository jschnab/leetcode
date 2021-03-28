# leetcode challenge 1790: check if one string swap can make 2 strings equal
# strings can be assumed to have the same length


def almost_equal1(s1, s2):
    """
    Return true if it is possible to make both strings equal by performing
    at most one swap of two characters one one of the strings.
    """
    diffs = 0
    length = len(s1)
    for i in range(length):
        if s1[i] != s2[i]:
            if diffs >= 2:  # too many inversions
                return False
            diffs += 1
            for j in range(length):
                if s2[j] == s1[i] and s2[i] == s1[j]:
                    break  # found inversion, continue
            else:
                return False
    return True


def almost_equal2(s1, s2):
    """
    Return true if it is possible to make both strings equal by performing
    at most one swap of two characters one one of the strings.
    """
    diffs = [[x, y] for x, y in zip(s1, s2) if x != y]
    return not diffs or len(diffs) == 2 and diffs[0][::-1] == diffs[1]


def test1():
    s1 = "abcd"
    s2 = "abcd"
    assert almost_equal1(s1, s2) is True
    assert almost_equal2(s1, s2) is True


def test2():
    s1 = "abcd"
    s2 = "dbca"
    assert almost_equal1(s1, s2) is True
    assert almost_equal2(s1, s2) is True


def test3():
    s1 = "abcd"
    s2 = "dcba"
    assert almost_equal1(s1, s2) is False
    assert almost_equal2(s1, s2) is False


def test4():
    s1 = "abcd"
    s2 = "efgh"
    assert almost_equal1(s1, s2) is False
    assert almost_equal2(s1, s2) is False


def main():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    main()
