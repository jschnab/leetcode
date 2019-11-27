# script which determines if a number is a palindrom without
# converting to string

def is_palindrome(number):
    """Determines if number is palindrome."""

    rev = 0
    while number > rev:
        rev = rev * 10 + number % 10
        number = number // 10
    if (rev == number) or (rev // 10 == number):
        return True
    else:
        return False

if __name__ == '__main__':
    number = int(input())
    print(is_palindrome(number))
