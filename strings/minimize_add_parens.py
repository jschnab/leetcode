"""
leetcode 2232: Minimize result by adding parentheses to expression.

We are given a string S with the format A+B where A and B are positive
integers.

We have to add a pair of parentheses to S such that after the addition of
parentheses, S is a valid mathematical expression and evaluates to the smallest
possible value. The left parenthesis must be added to the left of + and the
right parenthesis must be added to the right of +.

Return S after adding the pair of parenthesis, given the constraint above.
"""


def minimize_expression(S):
    """
    We want to minimize a mathematical expression that has the format
    a * (b + c) * d, given an input string with the format A+B. We have
    to find the position of ( within A to form a and b and ) within B to
    form c and d such that the expression is minimized.

    We simply try every combination of ( and ) position and determine which one
    minimizes the expression.
    """
    left, right = S.split("+")
    mini = float("inf")

    # i is the position of (
    for i in range(len(left)):
        a = int(left[:i]) if len(left[:i]) else 1
        b = int(left[i:])

        # j is the position of )
        for j in range(1, len(right) + 1):
            c = int(right[:j])
            d = int(right[j:]) if len(right[j:]) else 1
            calc = a * (b + c) * d
            if calc < mini:
                result = (
                    left[:i]
                    + "("
                    + left[i:]
                    + "+"
                    + right[:j]
                    + ")"
                    + right[j:]
                )
                mini = calc
    return result


def test1():
    assert minimize_expression("247+38") == "2(47+38)"
    print("test 1 successful")


def test2():
    assert minimize_expression("12+34") == "1(2+3)4"
    print("test 2 successful")


def test3():
    assert minimize_expression("999+999") == "(999+999)"
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
