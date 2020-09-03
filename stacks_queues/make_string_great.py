# leetcode challenge 1544: make the string great
# given a string of lower and uppercase english letters
# a 'good' string does not have two adjacent characters s[i] and s[i+1]
# where 0 <= i <= s.length - 2
# s[i] is a lower-case letter and s[i+1] is the same letter but upper-case
# or vice-versa
# to make the string good we choose two adjacent characters that make the
# string 'bad' and remove them
# return the string after making it good


def make_great(s):
    """
    Make the string great.

    Time complexity: O(n)
    Space complexity: O(n)

    :param str s: string to make great
    :returns: str - great string
    """
    stack = []
    for i in s:
        popped = False
        if stack:
            if abs(ord(stack[-1]) - ord(i)) == 32:
                stack.pop()
                popped = True
        if not popped:
            stack.append(i)
    return "".join(stack)
