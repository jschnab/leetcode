"""
leetcode 2266

One is texting using a phone with the following mapping between keys and
letters:
2: a, b, c
3: d, e, f
4: g, h, i
5: j, k, l
6: m, n, o
7: p, q, r, s
8: t, u, v,
9: w, x, y, z

In order to add a letter, one has to press the key of the corresponding digit
i times, where i is the position of the letter in the key.

Keys 0 and 1 do not map to letters, so they are not used.

Given a string of pressed keys such as "2266622", return the total number of
possible messages that could have been sent.

The answer is very large, so return it modulo 1e9 + 7.
"""


def count_texts(s):
    mod = 1e9 + 7
    memo = [0] * (len(s) + 1)
    memo[0] = 1
    for i in range(1, len(s) + 1):
        memo[i] = (memo[i] + memo[i - 1]) % mod
        if i - 2 >= 0 and s[i - 1] == s[i - 2]:
            memo[i] = (memo[i] + memo[i - 2]) % mod
            if i - 3 >= 0 and s[i - 1] == s[i - 3]:
                memo[i] = (memo[i] + memo[i - 3]) % mod
                if i - 4 >= 0 and s[i - 1] in "79" and s[i - 1] == s[i - 4]:
                    memo[i] = (memo[i] + memo[i - 4]) % mod
    return int(memo[-1])


def test1():
    assert count_texts("22233") == 8
    print("test 1 successful")


def test2():
    assert count_texts("222222222222222222222222222222222222") == 82876089
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
