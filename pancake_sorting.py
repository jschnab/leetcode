# script which performs pancake sorting

from random import randint


def pancake_sorting(A: list) -> list:
    """Sorts a list using pancake sorting."""
    l = len(A)

    # list of index of flips
    flips = []

    while l > 0:
        i_max = A.index(max(A[:l]))
        if i_max != 0:
            flips.append(i_max + 1)
        flips.append(l)
        A = A[:i_max + 1][::-1] + A[i_max + 1:]
        A[:l] = A[:l][::-1]
        l -= 1

    return A


if __name__ == "__main__":
    A = [randint(0, 100) for _ in range(5)]
    print("Input: ", A)
    print("Output: ", pancake_sorting(A))
