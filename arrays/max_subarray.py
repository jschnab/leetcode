def max_subarray(A):
    best_sum = float("-inf")
    cur_sum = 0
    for x in A:
        cur_sum += x
        if cur_sum > best_sum:
            best_sum = cur_sum
        if cur_sum < 0:
            cur_sum = 0
    return best_sum


def max_subarray_idx(A):
    best_sum = float("-inf")
    best_start = best_end = None
    cur_sum = 0
    cur_start = 0
    for cur_end, x in enumerate(A):
        if cur_sum <= 0:
            cur_sum = x
            cur_start = cur_end
        else:
            cur_sum += x
        if cur_sum > best_sum:
            best_sum = cur_sum
            best_start = cur_start
            best_end = cur_end
    return best_sum, best_start, best_end



def test1():
    assert max_subarray([1, 2, 3]) == 6


def test2():
    assert max_subarray([1, 2, -3, 2]) == 3


def test3():
    assert max_subarray([-3, -1, -2]) == -1


def test4():
    assert max_subarray_idx([1, 2, 3]) == (6, 0, 2)


def test5():
    assert max_subarray_idx([1, 2, -3, 2]) == (3, 0, 1)


def test6():
    assert max_subarray_idx([-3, -1, -2]) == (-1, 1, 1)


def test7():
    assert max_subarray_idx([-1, -3, 0]) == (0, 2, 2)


def test8():
    assert max_subarray_idx([-2, 1, -3, 4, -1, 2, 1]) == (6, 3, 6)


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
