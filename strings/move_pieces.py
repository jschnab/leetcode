"""
leetcode 2337: move pieces to obtain a string

We are given two string 'start' and 'end', both of length n. Each string only
consists of the characters L, R, and _:
- L and R represent pieces where L can move left only if there is a blank space
  directly to its left, and R can move right only if there is a blank space
  directly to its right
- the character _ represents a blank space that can be occupied by any or L or
  R.

Return True if it is possible to obtain the string 'end' by moving the pieces
of the string 'start' any number of times. Otherwise, return False.
"""


def move_pieces(start, end):
    """
    We solve this problem with two pointers.

    :param str start: Start string.
    :param str end: Target string.
    :returns (bool): True if we can convert start to end.
    """
    i = j = 0
    while i < len(start) or j < len(end):
        # advance the start pointer to the next character
        while i < len(start) and start[i] == "_":
            i += 1
        # advance the end pointer to the next character
        while j < len(end) and end[j] == "_":
            j += 1

        # check if piece movements are valid
        if (
            i == len(start)  # we finished iterating
            or j == len(end)  # we finished iterating
            or start[i] != end[j]  # characters are not in order
            or start[i] == "L" and i < j  # L piece moved right
            or start[i] == "R" and i > j  # R piece move left
        ):
            break
        i += 1
        j += 1

    # if we reached the end, then all piece movements were valid
    return i == j == len(start)


def test1():
    assert move_pieces("_L__R__R_", "L______RR") is True
    print("test 1 successful")


def test2():
    assert move_pieces("R_L_", "__LR") is False
    print("test 2 successful")


def test3():
    assert move_pieces("_R", "R_") is False
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
