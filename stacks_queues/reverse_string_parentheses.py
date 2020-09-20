# leetcode challenge 1190: reverse substrings between each pair of parentheses

# given a string s that consists of lowercase English letters and parentheses,
# reverse the strings in each pair of match parentheses, starting from the
# innermost one
# the result should not contain parentheses, only the letters


# input: (abcd)
# output: dcba

# input: (u(love)i)
# output: iloveu

# input: (ed(et(oc))el)
# output: leetcode

# input: (e(not(sk)cal)b)
# output: blackstone


def reverse_string(string):
    """
    Reverse strings between parentheses, starting with innermost strings.

    :param str string: string to reverse
    :returns: str - reversed string
    """
    stack = []
    for c in string:
        if c == ")":
            substack = []
            while stack[-1] != "(":
                substack.append(stack.pop())
            stack.pop()
            stack.extend(substack)
        else:
            stack.append(c)
    return "".join(stack)


def test1():
    string = "(abcd)"
    assert reverse_string(string) == "dcba"
    print("test 1 successful")


def test2():
    string = "(u(love)i)"
    assert reverse_string(string) == "iloveu"
    print("test 2 successful")


def test3():
    string = "(ed(et(oc))el)"
    assert reverse_string(string) == "leetcode"
    print("test 3 successful")


def test4():
    string = "(e(lac(sk)ton)b)"
    assert reverse_string(string) == "blackstone"
    print("test 4 successful")


def main():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    main()
