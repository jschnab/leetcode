"""
leetcode 2432: employee that worked on the longest task

There are n employees, each with a unique ID from 0 to n - 1.

We are given a 2D integer array logs where logs[i] = [id, leavTime] where:

* id is the ID of the employee that worked on the ith task
* leaveTime is the time at which the employee finished the ith task. All the
  values leaveTime are unique.

Note that the ith task starts at the moment right after the (i - 1)th task
ends, and the 0th task starts at time 0.

Return the ID of the employee that worked the task with the longest time. If
there is a tie between two or more employees, return the smallest ID among
them.
"""


def hardworker(n, logs):
    """
    We transform leaveTime into durations for tasks by subtracting the
    leaveTime of the previous task, i.e. the start time of the current task, in
    place.

    Then we simply sort logs by increasing task duration and decreasing ID.
    """
    last = logs[0][1]
    for i in range(1, len(logs)):
        tmp = logs[i][1]
        logs[i][1] -= last
        last = tmp
    return sorted(logs, key=lambda x: (x[1], -x[0]))[-1][0]


def test1():
    assert hardworker(10, [[0, 3], [2, 5], [0, 9], [1, 15]]) == 1
    print("test 1 successful")


def test2():
    assert hardworker(26, [[1, 1], [3, 7], [2, 12], [7, 17]]) == 3
    print("test 2 successful")


def test3():
    assert hardworker(2, [[0, 10], [1, 20]]) == 0
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
