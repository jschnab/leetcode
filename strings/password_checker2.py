"""
leetcode 2299: password checker 2

A password is said to be strong if it satisfies all the following criteria"
- at least 8 characters
- at least one uppercase letter
- at least one lowercase letter
- at least one digit
- at least one special character !@#$%^&*()-+
- it does not contain two of the same character in adjacent positions

Return true if the input string is a strong password, else return false.
"""


def is_strong(password):
    if len(password) < 8:
        return False
    special = set("!@#$%^&*()-+")
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    c1 = None
    for c in password:
        if c.isdigit():
            has_digit = True
        elif c in special:
            has_special = True
        else:
            has_lower |= c == c.lower()
            has_upper |= c == c.upper()
        if c1 and c1 == c:
            return False
        c1 = c
    return has_lower and has_upper and has_digit and has_special


def test1():
    assert is_strong("IloveLe3tcode!") == True
    print("test 1 successful")

def test2():
    assert is_strong("Me+You--IsMyDream") == False
    print("test 2 successful")

def test3():
    assert is_strong("1aB!") == False
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
