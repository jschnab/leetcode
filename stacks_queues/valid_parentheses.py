# leetcode 20
# determine if a string containing parentheses, square brackets
# and curly brackets are valid (closed if open, in the correct order)

# valid example: ([{}])()[]
# invalid example: ([)]

from collections import deque


def valid_parentheses(string):
    """
    Check if a string containing (), [] and {} is valid.

    Time complexity: O(n)
    Space complexity: O(n)

    :param str string: string to check the validity of
    :return bool: True if the string is valid else False
    """
    brackets = {"(": ")", "[": "]", "{": "}"}
    stack = deque()
    for char in string:
        if char in brackets:
            stack.append(char)
        else:
            it not stack or char != brackets[stack.pop()]:
                return False
    return not stack


if __name__ == "__main__":
    string1 = "([)]"
    print(f"Is {string1} valid? {valid_parentheses(string1)}")
    string2 = "()[]{[()]}"
    print(f"Is {string2} valid? {valid_parentheses(string2)}")
