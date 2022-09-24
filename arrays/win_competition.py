"""
leetcode 2283: minimum hours of training to win a competition

We are entering a competition and are given two positive integers 'energy' and
'experience' denoting initial energy and experience.

We are given two integer arrays A and B of the length n.

We will face n opponents in order. The energy of the ith opponent is A[i] and
experience of the ith opponent is B[i]. When we face an opponent, we need to
have both strictly greater experience and energy to defeat them and move to the
next opponent.

Defeating the ith opponent increases your experience by B[i] and decreases your
energy by A[i].

Before starting the competition, we can train for some number of hours. After
each hour of training, we can either choose to increase initial experience by
one, or increase initial energy by one.

Calculate the minimum number of training hours required to defeat all
opponents.
"""


def training(energy, experience, A, B):
    result = max(0, sum(A) - energy + 1)
    for opponent in B:
        if experience < opponent:
            result += opponent - experience + 1
            experience += 2 * opponent - experience + 1
        else:
            experience += opponent
    return result


def test1():
    assert training(5, 3, [1, 4, 3, 2], [2, 6, 3, 1]) == 8
    print("test 1 successful")


def test2():
    assert training(2, 4, [1], [3]) == 0
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
