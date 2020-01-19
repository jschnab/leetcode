# biweekly contest 17 problem 1313
# decompress run-length encoding of integer list
# Input: [1, 2, 3, 4], Output: [2, 4, 4, 4]

def decompress_run_length(array):
    """
    Decompress run-length encoded array of integers.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    answer = []
    for i in range(0, len(array), 2):
        answer.extend([array[i + 1]] * array[i])
    return answer


def decompress_run_length2(array):
    """
    Decompress run-length encoded array of integers.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    answer = []
    i = 0
    while 2 * i + 1 < len(array):
        answer.extend([array[2 * i + 1]] * array[2 * i])
        i += 1
    return answer


if __name__ == "__main__":
    array = [1, 2, 3, 4]
    print("Input: ", array)
    print("Output: ", decompress_run_length(array))
