from random import choices, randint


def add_binaries(a, b):
    """
    Add two binary numbers.
    """

    # we want a to be the higher number
    la = len(a)
    lb = len(b)
    if lb > la:
        a, b = b, a

    i = la - 1
    j = lb - 1
    carry = 0
    answer = ''

    # sum numbers while there are bits on the smallest
    while j >= 0:
        cur = int(a[i]) + int(b[j]) + carry
        answer = str(cur % 2) + answer
        if cur > 1:
            carry = 1
        else:
            carry = 0
        i -= 1
        j -= 1

    # sum remaining bits from the longest
    while i >= 0:
        cur = int(a[i]) + carry
        answer = str(cur % 2) + answer
        if cur > 1:
            carry = 1
        else:
            carry = 0
        i -= 1

    if carry:
        answer = '1' + answer
    return answer


def binary_to_decimal(number):
    """
    Converts a binary number into a decimal number.
    This function does not check if the string is only made of ones and zeros.

    :param str number: string representing a binary number, e.g. '1011'
    :return int: integer conversion
    """
    l = len(number) - 1
    i = 0
    integer = 0

    while l >= 0:
        if number[l] == '1':
            integer += 2 ** i
        i += 1
        l -= 1

    return integer


def decimal_to_binary(number):
    """
    Converts a decimal number to binary.

    :param int: decimal number
    :return str: string representing a binary number
    """
    if number == 0:
        return "0"
    binary = ""
    while number != 0:
        remaining = number % 2
        if remaining == 1:
            binary = "1" + binary
        else:
            binary = "0" + binary
        number //= 2
    return binary
