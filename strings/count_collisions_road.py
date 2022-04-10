"""
leetcode 2211: Count collisions on a road.

There are `n` cars on an infinitely long road. Cars are numbered 0 to n - 1
from left to right and each car is present a unique point.

Given a string `directions` of length `n`, `directions[i]` can be either `L`,
`R` or `S`, indicating whether the ith car is moving towards the left, right,
or staying at its current point. Each car moves at the same speed.

The number of collisions can be calculated as follows:

- When to cars move in opposite directions collide with each other, the number
of collisions is increased by 2.
- When a moving car collides with a stationary car, the number of collisions
is increased by 1.

After a collision, the cars involved can no longer move and will stay where
they collided. Other than that, cars cannot change their state or direction of
motion.

Return the total number of collisions.
"""


def collisions(directions):
    """
    We count collisions from left to right by keeping two pointers.

    To account for a sequence of cars moving right, we also count how many
    right-moving cars we encountered.

    Time complexity: O(n).
    Space complexity: O(1).
    """
    prev = directions[0]
    r = 0  # keep track of how many R we encountered
    if prev == "R":
        r = 1
    col = 0
    for d in directions[1:]:
        if d == "L":
            if prev == "R":
                col = col + 2 + r - 1
                r = 0
                prev = "S"  # cars do not move after collision
            elif prev == "S":
                col += 1
            else:
                prev = d
        elif d == "S":
            if prev == "R":
                col += r  # col + 1 and r - 1 cancel ones out
                r = 0
                prev = "S"
            else:
                prev = d
        else:
            r += 1
            prev = d
    return col


def test1():
    assert collisions("RLRSLL") == 5
    print("test 1 successful")


def test2():
    assert collisions("LLRR") == 0
    print("test 2 successful")


def test3():
    assert collisions("RLRRRSL") == 6
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
