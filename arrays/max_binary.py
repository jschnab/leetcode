# maximum binary string after changes: leetcode 1702
# given a binary string (0s and 1s only), we can apply two operations
# any number of times:
# - replace 00 with 10
# - replace 10 with 01

# return the maximum binary string (based on decimal representaiton) we can
# obtain after any number of any operation

# the idea is to ignore the first streak of 1s if it exist, they already are
# part of the result
# then we turn all following 10 into 01, to make a series of 0s
# finally, we turn all the 00 into 10, going from left to right
# these operations can be simplified into a mathematical form


def max_binary(s):
    if "0" not in s:
        return s
    first_zero = s.find("0")  # index of the first 0
    n0 = s.count("0", first_zero)  # count number of 0s after 1s
    n1 = len(s) - first_zero - n0  # count number of 1s after 1s and 0s
    return "1" * first_zero + "1" * (n0 - 1) + "0" + "1" * n1


def test1():
    s = "000110"
    assert max_binary(s) == "111011"


def test2():
    s = "111"
    assert max_binary(s) == "111"


def test3():
    s = "10001100"
    assert max_binary(s) == "11111011"


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
