def clear_ms_through_i(number, i):
    print("before:", bin(number))
    mask = (1 << i) - 1
    print("mask:", bin(mask))
    print("after:", bin(number & mask))
    print()


def clear_i_through_0(number, i):
    print("before:", bin(number))
    mask = ~((1 << i)  - 1)
    print("mask:", bin(mask))
    print("after:", bin(number & mask))
    print()


def test1():
    clear_ms_through_i(15, 2)


def test2():
    clear_i_through_0(15, 2)


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
