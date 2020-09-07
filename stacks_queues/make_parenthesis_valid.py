# leetcode challenge 921: minimum add to make parentheses valid
# given a string of '(' and ')', we add the minimum number of parentheses
# so that the resulting parentheses string is valid
# return the minimum number of parentheses we must add to make the
# string valid


def make_valid(S):
    non_closed = 0  # number of non-closed parentheses
    stack = []
    for i in S:
        if i == ")":
            # if the stack is empty, this closing parenthesis has no opening
            if len(stack) == 0:
                non_closed += 1
            # if the top of the stack is not an opening parenthesis, this
            # closing parenthesis has no opening
            else:
                if stack.pop() != "(":
                    non_closed += 1
        else:
            stack.append(i)

    # the stack may still contain parentheses that have not been closed
    return non_closed + len(stack)


def test1():
    S = "())"
    assert make_valid(S) == 1
    print("test 1 successful")


def test2():
    S = "((("
    assert make_valid(S) == 3
    print("test 2 successful")


def test3():
    S = "()"
    assert make_valid(S) == 0
    print("test 3 successful")


def test4():
    S = "()))(("
    assert make_valid(S) == 4
    print("test 4 successful")


def main():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    main()
