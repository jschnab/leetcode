# leetcode challenge 856: score of parentheses

# given a balanced parentheses string S, calculate the score of the string
# based on the following rules:
# - () has a score of 1
# - AB has score A + B where A and B are valid parentheses strings
# - (A) has score 2 * A where A is a balanced parentheses string

# input: "()"
# output: 1

# input: "(())"
# output: 2

# input: "()()"
# output: 2

# input: "(()(()))"
# output: 6


def score_parentheses1(string):
    """
    A balanced string is 'primitive' if it cannot be partitioned into two
    non-empty balanced strings. By keeping track of the balance (number of
    opened parentheses), we partition the string into primitive substrings P
    string = P1 + P2 ... + Pn. Then score(string) = score(P1) + score(P2) ...
    For each primitive substring, if the string is length 2, then the score of
    this string is 1, otherwise it's twice the score of the substring.

    Time complexity: O(n2) where n is length of the string. The worst case is
    like (()).
    Space complexity: O(n), the size of the call stack.

    :param str string: string of parentheses
    :returns: int - score of the string
    """
    return helper(string, 0, len(string))

def helper(string, i, j):
    """
    Helper function for `score_parentheses1()`to recursively partition the
    string into primitives.

    :param str string: string to partition
    :param int i: index to start iteration
    :param int j: index to stop iteration
    :returns: int - score of string
    """
    score = 0
    balance = 0

    for k in range(i, j):

        # adjust the balance
        if string[k] == "(":
            balance += 1
        else:
            balance -= 1

        # update the score
        if balance == 0:

            # we have ()
            if k - i == 1:
                score += 1

            # we need to partition the string further
            else:
                score += 2 * helper(string, i+1, k)

            i = k + 1

    return score


def score_parentheses2(string):
    """
    Every position in the string has a depth, i.e. the number of parentheses
    surrounding it. For example, the dot in (()(.())) has a depth of 2 (the
    depth of the outermost parentheses is 0.

    We can keep track of our depth with a stack. When we have an opening
    parenthesis, we increase depth and the score at the new depth is 0. When
    we have a closing parenthesis, we add twice the current score at the
    current depth to the score at the deeper part (except when counting ()
    which has a score of 1).

    Time complexity: O(n) since we iterate once through the string
    Space complexity: O(n) because of the stack, which has size n

    :param str string: string to score
    :returns: int - score of the string
    """
    stack = [0]
    for p in string:
        if p == "(":
            stack.append(0)
        else:
            # if we score '()' we will pop 0, so make sure it's 1
            popped = stack.pop()
            stack[-1] += max(2 * popped, 1)
    return stack.pop()


def score_parentheses3(string):
    """
    We know the score must be a power of 2, since () has a score of 1 and
    it will have its score multiplied by 2 for each surrounding parentheses.

    We keep track of the parentheses balance. For every ')' that follows a '('
    the score is 1 << balance.

    Time complexity: O(n)
    Space complexity: O(1) since we directly update the score
    """
    score = 0
    balance = 0
    for i, p in enumerate(string):
        if p == "(":
            balance += 1
        else:
            balance -= 1
            if string[i-1] == "(":
                score += 1 << balance
    return score


def test1():
    s = "()"
    assert score_parentheses1(s) == 1
    assert score_parentheses2(s) == 1
    assert score_parentheses3(s) == 1
    print("test 1 successful")


def test2():
    s = "(())"
    assert score_parentheses1(s) == 2
    assert score_parentheses2(s) == 2
    assert score_parentheses3(s) == 2
    print("test 2 successful")


def test3():
    s = "()()"
    assert score_parentheses1(s) == 2
    assert score_parentheses2(s) == 2
    assert score_parentheses3(s) == 2
    print("test 3 successful")


def test4():
    s = "(()(()))"
    assert score_parentheses1(s) == 6
    assert score_parentheses2(s) == 6
    assert score_parentheses3(s) == 6
    print("test 4 successful")



def main():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    main()
