from collections import Counter

"""
leetcode 2244: Minimum rounds to complete all tasks.

You are given an array A containing integers, where A[i] represents the
difficulty level of a task. In each round, we can complete 2 or 3 tasks of the
same difficulty level.

Calculate the mininum number of rounds required to complete all tasks, or -1
if it's not possible to complete all tasks.
"""


def complete_tasks(A):
    counts = Counter(A)
    result = 0
    for level, ntasks in counts.items():
        if ntasks < 2:
            return -1
        else:
            if ntasks >= 5:
                rem = ntasks % 3
                if rem == 0:
                    result += ntasks // 3
                    continue
                if rem == 1:
                    result += (ntasks // 3) - 1
                    ntasks = 4
                else:
                    result += ntasks // 3
                    ntasks = 2
            if ntasks == 4:
                result += 2
            else:
                result += 1
    return result


def test1():
    assert complete_tasks([2, 2, 3, 3, 2, 4, 4, 4, 4, 4]) == 4
    print("test 1 successful")


def test2():
    assert complete_tasks([2, 3, 3]) == -1
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
