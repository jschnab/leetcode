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
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = deque()
    for i in string:
        if i in pairs:
            if stack.pop() != pairs[i]:
                return False
        else:
            stack.append(i)
    return not stack


if __name__ == "__main__":
    string1 = "([)]"
    print(f"Is {string1} valid? {valid_parentheses(string1)}")
    string2 = "()[]{[()]}"
    print(f"Is {string2} valid? {valid_parentheses(string2)}")
