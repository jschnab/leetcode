def subarray_sum(array, s):
    result = 0
    for i in range(len(array)):
        sum_ = 0
        for j in range(i, len(array)):
            sum_ += array[j]
            if sum_ == s:
                result += 1
    return result


def test1():
    assert subarray_sum([1, 1, 1], 2) == 2
    print("test 1 successful")


def test2():
    assert subarray_sum([1, 1, 1], 3) == 1
    print("test 2 successful")


def test3():
    assert subarray_sum([1, 2, 3], 3) == 2
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
