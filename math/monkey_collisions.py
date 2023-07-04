"""
leetcode 2550: count collisions of monkeys on a polygon

There is a regular convex polygon with n vertices. The vertices are labeled
from 0 to n - 1 in a clockwise direction, and each vertex has exactly one
monkey.

Each monkey moves simultaneously to a neighboring vertex. A neighboring vertex
i can be:

    * the vertex (i + 1) % n in the clockwise direction.
    * the vertex (i - 1 + n) % n in a counter-clockwise direction.

A collision happens if at least two monkeys reside on the same vertex after the
movement or intersect on an edge.

Return the number of ways the monkeys can move so that at least one collision
happens. Since the answer may be large, return it modulo 10^9 + 7.

Note that each monkey can move only once.
"""


def collisions(n):
    """
    There are only two ways for monkeys to move without a collision: if all
    monkeys move in the same direction, either clockwise or counter-clockwise.

    Because there are n monkeys and each can move in either direction, the
    total number of possible move (collision or not) is 2 ^ n. The solution to
    the problem is then 2 ^ n - 2.

    However, large powers take a long time to calculate. Fortunately, Python
    allows to calculate a power with a modulus, with the built-in function
    pow().
    """
    mod = 1000000007
    return (pow(2, n, mod) - 2) % mod
