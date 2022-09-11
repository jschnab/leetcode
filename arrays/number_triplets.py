"""
leetcode 2367: number of arithmetic triplets

We are given a strictly increasing integer array A and a positide integer d. A
triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

* i < j < k
* A[j] - A[i] = d
* A[k] = A[j] = d

Return the number of unique arithmetic triplets.
"""


def triplets(A, d):
    result = 0
    s = set(A)
    for n in s:
        if n - d in s and n + d in s:
            result += 1
    return result


def test1():
    assert triplets([0, 1, 4, 6, 7, 10], 3) == 2
    print("test 1 successful")


def test2():
    assert triplets([4, 5, 6, 7, 8, 9], 2) == 2
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
