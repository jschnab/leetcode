# leetcode challenge 1249: minimum remove to make valid parentheses
# given a string or '(' and ')', and lowercase English characters, we
# have to remove the minimum number of parentheses so that the resulting
# parentheses string is valid
# there are sometimes several valid solutions, return any
# a parentheses string is valid iff:
# - it is empty, contains only lowercase characters, or
# - it can be written as A + B where A and B are valid strings and '+'
#   is the concatenation of strings
# - it can be written as (A) where A is a valid string

# input:  "lee(t(c)o)de)"
# output: "lee(t(c)o)de" or "lee(t(c)ode)"

# input:  "a)b(c)d"
# output: "ab(c)d"

# input:  "))(("
# output: ""

# input:  "(a(b(c)d)"
# output: "a(b(c)d)"

from collections import deque


def min_del_parentheses(s):
    """
    Remove the minimum number of parentheses to make a valid string.

    :param str s: string to process
    :returns: str - processed string
    """
    result = []
    temp = deque()  # use a deque object to append left with O(1)

    # remove unnecessary '('
    closed = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] == ")":
            closed += 1
            temp.appendleft(s[i])
        elif s[i] == "(":
            if closed > 0:
                closed -= 1
                temp.appendleft(s[i])
        else:
            temp.appendleft(s[i])

    # remove unnecessary ')'
    opened = 0
    for c in temp:
        if c == "(":
            result.append(c)
            opened += 1
        elif c == ")":
            if opened > 0:
                result.append(c)
                opened -= 1
        else:
            result.append(c)

    return "".join(result)


def test1():
    string = "lee(t(c)o)de)"
    expected = ("lee(t(c)o)de", "lee(t(co)de)", "lee(t(c)ode)")
    assert min_del_parentheses(string) in expected
    print("test 1 successful")


def test2():
    string = "a)b(c)d"
    expected = "ab(c)d"
    assert min_del_parentheses(string) == expected
    print("test 2 successful")


def test3():
    string = "))(("
    expected = ""
    assert min_del_parentheses(string) == expected
    print("test 3 successful")


def test4():
    string = "(a(b(c)d)"
    expected = ("(a(bc)d)", "a(b(c)d)", "(ab(c)d)")
    assert min_del_parentheses(string) in expected
    print("test 4 successful")


def main():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    main()
