"""
leetcode 2326: spiral matrix IV

We are given two integers m and n, that represent the dimensions of a matrix.
We are also given the head of a linked list of integers.

Generate an m* n matrix that contains the integers of the linked list presented
in spiral order (clockwise), starting from the top-left of the matrix. If there
are remaining empty spaces, fill them with -1.

Return the generated matrix.
"""


class Node:

    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


def spiral(m, n, head):
    """
    Make a spiral matrix.

    :param int m: Number of rows.
    :param int n: Number of columns.
    :param Node head: Head of a linked list.
    """
    # make a matrix that will be filled
    matrix = [[-1] * n for m in range(m)]

    # array of values to increment row and column indexes
    # for each i from 0 to 4, i = row index and i + 1 = column index
    direction = [0, 1, 0, -1, 0]

    # start filling the matrix from the top left
    i = j = d = 0

    while head:
        matrix[i][j] = head.val
        head = head.next
        # ni and nj are the next value for i and j
        ni = i + direction[d]
        nj = j + direction[d + 1]
        # check if we went outside the matrix, or if we went on a previously
        # filled cell
        # if we did, then we change direction
        if min(ni, nj) < 0 or ni == m or nj == n or matrix[ni][nj] != -1:
            d = (d + 1) % 4
        i += direction[d]
        j += direction[d + 1]
    return matrix


def test1():
    head = Node(0, Node(1, Node(2)))
    assert spiral(1, 4, head) == [[0, 1, 2, -1]]
    print("test 1 successful")


def test2():
    head = Node(5, Node(4, Node(3, Node(2, Node(1, Node(0))))))
    assert spiral(3, 3, head) == [[5, 4, 3], [-1, -1, 2], [-1, 0, 1]]
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
