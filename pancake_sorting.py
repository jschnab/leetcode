# script which performs pancake sorting

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

