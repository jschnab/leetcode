# given a list containing nested lists, flatten it


# this does not work for multiple levels
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            for j in i:
                result.append(j)
        else:
            result.append(i)
    return result


def flatten_recur(lst, result):
    for i in lst:
        if isinstance(i, list):
            flatten_recur(i, result)
        else:
            result.append(i)


def test1():
    a = [1, 2, 3, 4]
    assert flatten(a) == a
    print("test 1 successful")


def test2():
    a = [1, [2, 3], 4]
    assert flatten(a) == [1, 2, 3, 4]
    print("test 2 successful")


def test3():
    a = [1, 2, 3, 4]
    result = []
    flatten_recur(a, result)
    assert result == a
    print("test 3 successful")


def test4():
    a = [1, [2, 3], 4]
    result = []
    flatten_recur(a, result)
    assert result == [1, 2, 3, 4]
    print("test 4 successful")


def test5():
    a = [1, [2, [3, 4], 5], 6]
    result = []
    flatten_recur(a, result)
    assert result == [1, 2, 3, 4, 5, 6]
    print("test 5 successful")


def main():
    test1()
    test2()
    test3()
    test4()
    test5()


if __name__ == "__main__":
    main()
