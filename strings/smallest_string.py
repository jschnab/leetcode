"""
leetcode 2434: using a robot to print the lexicographically smallest string.

We are given a string S and a robot that currently holds an empty string T.
Apply one of the following operations until S and T are both empty:

* Remove the first character of a string S and give it to the robot. The robot
will append this character to the string T.

* Remove the last character of a string T and give it to the robot. The robot
will write this character on paper.

Return the lexicographically smallest string that can be written on the paper.
"""
from collections import Counter


def print_string(S):
    """
    We count each character in the string S. We iterate through S characters
    and put them in a stack. Each time we add a character to the stack, we find
    the next smallest character from S. While the top of the stack contains
    characters smallest than the smallest left in S, we print them from the
    stack and continue until the stack is empty or a larger character appears.
    """
    count = Counter(S)
    low = "a"
    stack = []
    paper = []
    for ch in S:
        stack.append(ch)
        count[ch] -= 1
        while low < "z" and count[low] == 0:
            low = chr(ord(low) + 1)
        while stack and stack[-1] <= low:
            paper.append(stack.pop())
    return "".join(paper)


def test1():
    assert print_string("zza") == "azz"
    print("test 1 successful")


def test2():
    assert print_string("bac") == "abc"
    print("test 2 successful")


def test3():
    assert print_string("bdda") == "addb"
    print("test 3 successful")


def main():
    test1()
    test2()
    test3()


if __name__ == "__main__":
    main()
