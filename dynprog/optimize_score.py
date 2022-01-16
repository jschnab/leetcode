import functools

"""
We have a 2D array 'questions' where questions[i]
is an array [points, brainpower], and we have to process questions
in the order they are given in the array, by either answering the
current question and earning the points, or skipping to the next
question. Answering a question consumes brainpower so you have to skip
the next brainpower questions after answering.

The goal is to determine the maximum possible score that can be obtained
by answering or skipping questions in the array.
"""


def max_score_recur(questions):
    """
    Recursively solve the problem using memoization.
    """
    def helper(i, memo):
        if memo.get(i) is not None:
            return memo.get(i)
        if i > len(questions) - 1:
            return 0
        maxi = max(
            questions[i][0] + helper(i + 1 + questions[i][1], memo),  # answer
            helper(i + 1, memo)  # skip
        )
        memo[i] = maxi
        return maxi

    return helper(0, {})


def max_score_recur2(questions):
    @functools.lru_cache()
    def helper(i):
        if i > len(questions) - 1:
            return 0
        return max(
            questions[i][0] + helper(i + questions[i][1] + 1),  # answer
            helper(i + 1)  # skip
        )
    return helper(0)


def max_score_iter(questions):
    """
    Iteratively solve the problem in a bottom-up fashion.
    """
    # assume brainpower values don't index further than twice the size
    # of the input array
    solution = [0] * 2 * (len(questions) + 1)
    for i in reversed(range(len(questions))):
        solution[i] = max(
            questions[i][0] + solution[i + questions[i][1] + 1],  # answer
            solution[i + 1]  # skip
        )
    return solution[0]


def test1():
    q = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
    solution = 7
    assert max_score_recur(q) == solution
    assert max_score_recur2(q) == solution
    assert max_score_iter(q) == solution


def main():
    test1()


if __name__ == "__main__":
    main()
