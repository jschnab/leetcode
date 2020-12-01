# leetcode challenge 1277: count square submatrices with all ones
# given an m * n matrix, return the number of square submatrices
# of any size where all elements are 1


def count_squares_dp1(matrix):
    if not matrix or len(matrix) == 0:
        return 0

    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    result += 1
                else:
                    cell_val = min(
                        matrix[i][j],
                        matrix[i-1][j],
                        matrix[i-1][j-1]
                    ) + 1
                    result += cell_val
                    matrix[i][j] = cell_val
    return result


def count_squares_dp2(matrix):
    """
    A dynamic programming approach.
    matrix[i][j] stores:
        - the maximum size of square where right-bottom corner is matrix[i][j]
        - the number of squares where right-bottom corner is matrix[j][j]
    """
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            matrix[i][j] *= min(
                matrix[i-1][j],
                matrix[i][j-1],
                matrix[i-1][j-1]
            ) + 1
    return sum(map(sum, matrix))


def count_squares_brute(matrix):
    result = 0
    m = len(matrix)
    n = len(matrix[0])
    max_size = max(2, min(m, n))
    for size in range(1, max_size + 1):
        for i in range(0, m - size + 1):
            for j in range(0, n - size + 1):
                zeros = False
                for k in range(i, i + size):
                    for l in range(j, j + size):
                        if matrix[k][l] == 0:
                            zeros = True
                if not zeros:
                    result += 1
    return result
