"""
leetcode 2201: Count artifacts that can be extracted

An n x n grid contains artifacts buried in it.
We are given the integer n and a 2D array of integers named
'artifacts' describing the position of rectangular artifacts
where artifacts[i] = (r1i, c1i, r2i, c2i) denotes the ith artifact
buried in the grid. (r1i, c1i) are the row and column indices of the
top-left cell of the ith artifact and (r2i, c2i) are the row and column
indices of the bottom-right cell of the ith artifact.

We excavate some cells of the grid. If the cell has a part of an artifact
buried underneath, it will be uncovered. If all parts of an artifact are
uncovered, we can extract it.

Given a 2D array 'dig' where dig[i] = (ri, ci) indicates that we will
excavate the cell (ri, ci), return the number of artifacts we can extract.

No artifact overlaps.
Each artifact is rectangular (square included).
"""


def dig_artifacts(n, artifacts, dig):
    """
    We generate a list of artifacts size. The size is an integer that
    represents the number of cells occupied by an artifact.

    We generate a dictionary that maps a cell of the grid to an artifact index.

    Then, we iterate through the dig array and decrement the array of artifact
    sizes each time we find an artifact (thanks to the cell-to-artifact map).
    When the size reaches zero, this means we excavated a full artifact.
    """
    # build the list of artifact sizes and the map from cell to artifact index
    buried_size = [0] * len(artifacts)
    cells_to_artifacts = [[None for _ in range(n)] for _ in range(n)]
    for idx, (r1, c1, r2, c2) in enumerate(artifacts):
        for row in range(r1, r2 + 1):
            for col in range(c1, c2 + 1):
                cells_to_artifacts[row][col] = idx
                buried_size[idx] += 1

    # start digging for artifacts
    result = 0
    for r, c in dig:
        artifact_idx = cells_to_artifacts[r][c]
        if artifact_idx is not None:
            buried_size[artifact_idx] -= 1
            if buried_size[artifact_idx] == 0:
                result += 1
    return result


def test1():
    n = 2
    artifacts = [[0, 0, 0, 0], [0, 1, 1, 1]]
    dig = [[0, 0], [0, 1]]
    assert dig_artifacts(n, artifacts, dig) == 1
    print("test 1 successful")


def test2():
    n = 2
    artifacts = [[0, 0, 0, 0], [0, 1, 1, 1]]
    dig = [[0, 0], [0, 1], [1, 1]]
    assert dig_artifacts(n, artifacts, dig) == 2
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
