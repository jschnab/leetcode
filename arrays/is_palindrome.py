# determine if a string is a palindrome


def is_palindrome(s):
    """
    :param str s: string to check
    :returns: bool - True if s is a palindrom else False
    """
    if len(s) == 0 or len(s) == 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False


def test1():
    s = ""
    assert is_palindrome(s)
    print("test 1 successful")


def test2():
    s = "a"
    assert is_palindrome(s)
    print("test 2 successful")


def test3():
    s = "hello"
    assert not is_palindrome(s)
    print("test 3 successful")


def test4():
    s = "kayak"
    assert is_palindrome(s)
    print("test 4 successful")


def main():
    test1()
    test2()
    test3()
    test4()


if __name__ == "__main__":
    main()
