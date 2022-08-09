"""
leetcode 2327: number of people aware of a secret

On day 1, one person discovers a secret.

We are given an integer 'delay' that means that each person will share the
secret with a new person every day, startin from 'delay' days after discovering
the secret.

We are also given an integer 'forget', that means that each person will forget
the secret 'forget' days after discovering it.

A person cannot share the secret on the same day they forgot it, or on any day
after.

Given an integer n, return the number of people who know the secret at the end
of day n. Since the answer may be very large, return it modulo 1e9 + 7.
"""


def secret(n, delay, forget):
    """
    """
    # timeline stores the number of people who know the secret on each day
    timeline = [0] * n
    timeline[0] = 1

    for i in range(n):
        if timeline[i] > 0:
            # for each person who know the secret on day i, they will share it
            # between days i + delay and i + forget (mind the array end)
            for j in range(i + delay, min(n, i + forget)):
                timeline[j] += timeline[i]

    # calculate the number of people who know the secret on the last day
    result = 0
    for i in range(n):
        # if they forget after the last day, they know it on the last day
        if i + forget >= n:
            result += timeline[i]
    return result % 1000000007


def test1():
    assert secret(6, 2, 4) == 5
    print("test 1 successful")


def test2():
    assert secret(4, 1, 3) == 6
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
