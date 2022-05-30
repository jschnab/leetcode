"""
leetcode 2266: Count number of texts.
"""


def count_texts(s):
    """
    I don't quit understand this one.
    """
    memo = [1] * 5
    for i in reversed(range(len(s))):
        #print("i =", i)
        memo[i % 5] = 0
        #print("memo =", memo)
        if s[i] in '79':
            k = 4
        else:
            k = 3
        max_j = min(len(s), i + k)
        #print("max_j =", max_j)
        for j in range(i, max_j):
            #print("j =", j)
            if s[i] != s[j]:
                #print(f"{s[i]} != {s[j]}, breaking")
                break
            #print(f"memo[{i % 5}] = memo[{i % 5}] + memo[{(j + 1) % 5}]")
            memo[i % 5] = (memo[i % 5] + memo[(j + 1) % 5]) % (1e9 + 7)
            #print("memo =", memo)
            #print()
    return int(memo[0])


def count_texts2(s):
    """
    """
    mod = 1e9 + 7
    memo = [0] * (len(s) + 1)
    memo[0] = 1
    for i in range(1, len(s) + 1):
        memo[i] = (memo[i] + memo[i - 1]) % mod
        if i - 2 >= 0 and s[i - 1] == s[i - 2]:
            memo[i] = (memo[i] + memo[i - 2]) % mod
            if i - 3 >= 0 and s[i - 1] == s[i - 3]:
                memo[i] = (memo[i] + memo[i - 3]) % mod
                if s[i - 1] in "79" and i - 3 >= 0 and s[i - 1] == s[i - 4]:
                    memo[i] = (memo[i] + memo[i - 4]) % mod
    return int(memo[-1])


def test1():
    assert count_texts("22233") == 8
    assert count_texts2("22233") == 8
    print("test 1 successful")


def test2():
    assert count_texts("7777") == 8
    assert count_texts2("7777") == 8
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
