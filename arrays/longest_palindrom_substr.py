# leetcode 5
# find the longest palindromic substring in a string
# dbracecarple returns racecar

def long_pal_brute(s):
    """Return longest palindromic substring.
    Time complexity is O(n^3)."""
    l = len(s)
    if l < 2:
        return s
    answer = ''
    for i in range(l):
        for j in range(i):
            if s[j:i+1] == s[j:i+1][::-1]:
                if i - j + 1 > len(answer):
                    answer = s[j:i+1]
    if answer:
        return answer
    else:
        return s[0]

def long_pal(s):
    """Return longest string with dynamic programming approach.
    Time and space complexity are both O(n^2)."""
    ans = ''
    l = len(s)
    max_l = 0

    # we generate an n x n table to store where we found palindromes
    memo = [[0] * l for _ in range(l)]

    # we first store 1-letter palindromes
    for i in range(l):
        memo[i][i] = 1
        ans = s[i]
    max_l = 1

    # we then store eventual 2-letter palindromes
    for i in range(l-1):
        if s[i] == s[i+1]:
            memo[i][i+1] = 1
            ans = s[i:i+2]
    max_len = 2

    # now we extend our search for >= 3-letter palindromes
    for j in range(l):
        for i in range(j-1):
            if s[i] == s[j] and memo[i+1][j-1]:
                memo[i][j] = 1
                if j - i + 1 > max_len:
                    max_len = j - i + 1
                    ans = s[i:j+1]
    return ans

if __name__ == '__main__':
    print('radar : ', long_pal('radar'))
    print('dbracecarple : ', long_pal('dbracecarple'))
    print(' : ', long_pal(''))
    print('ab : ', long_pal('ab'))
