"""
leetcode 2433: find the original array of prefix XOR

We are given an integer array P of size n. Find and return the array A of size
n that satisfies: P[i] = A[0] XOR A[1] XOR ... XOR A[i].

It can be proven that the answer is unique.
"""


def original(P):
    """
    We use the 'reversibility' property of XOR: A XOR B = C <=> B XOR C = A.
    """
    result = [P[0]]
    for i in range(1, len(P)):
        result.append(P[i - 1] ^ P[i])
    return result


def test1():
    assert original([5, 2, 0, 3, 1]) == [5, 7, 2, 3, 2]
    print("test 1 successful")


def test2():
    assert original([13]) == [13]
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
