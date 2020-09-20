# leetcode challenge 1021: remove outermost parentheses

# a valid parentheses string is either:
# - empty ('')
# - '(' + A + ')'
# - A + B (where A and B are valid parentheses strings and '+' is concat)

# a valid parentheses string is primitive if it is non-empty and there does
# exist a way to split it into A + B where A and B are non-empty valid 
# parentheses string

# given a valid parentheses string S composed of the concatenation of
# primitive valid parentheses strings, remove from S the outermost
# parentheses of every primitive in S

# input: (()())(())
# decomposition: (()()) + (())
# output: ()()()

# input: (()())(())(()(()))
# decomposition: (()()) + (()) + (()(()))
# output: ()()()()(())

# input: ()()
# decomposition: () + ()
# output: null


def is_primitive(L):
    """
    Determine if list makes a primitive string.

    :param list[str] L: list of characters of a string
    :returns: bool - True if string is primitive else False
    """
    stack = []
    for i, c in enumerate(L):
        if c == "(":
            stack.append(c)
        else:
            stack.pop()
            # if we closed all parentheses before reaching the
            # end of the input list, it's not a primitive
            if len(stack) == 0 and i < len(L) - 1:
                return False

    # if there are still open parentheses after we finish iterating,
    # its not a primitive
    if stack:
        return False

    return True


def remove_parens(S):
    stack = []
    result = []
    for c in S:
        stack.append(c)
        if c == ")":
            if len(stack) % 2 == 0 and is_primitive(stack):
                result.extend(stack[1:-1])
                stack = []
    return "".join(result)


def remove_parens2(S):
    result = []
    opened = 0  # count the number of opened parentheses
    for c in S:
        if c == "(":
            if opened > 0:  # we don't append the outer '('
                result.append(c)
            opened += 1
        elif c == ")":
            if opened > 1:  # we don't append the outer ')'
                result.append(c)
            opened -= 1
    return "".join(result)


def test1():
    S = "(()())(())"
    assert remove_parens(S) == "()()()"
    assert remove_parens2(S) == "()()()"
    print("test 1 successful")


def test2():
    S = "(()())(())(()(()))"
    assert remove_parens(S) == "()()()()(())"
    assert remove_parens2(S) == "()()()()(())"
    print("test 2 successful")


def test3():
    S = "()()"
    assert remove_parens(S) == ""
    assert remove_parens2(S) == ""
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
