def strcmp(s, t):
    """
    Return < 0 if s < t, 0 if s == t, > 0 if s > t

    :param str s: first string to compare
    :param str t: second string to compare
    :returns: int
    """
    len_s = len(s)
    len_t = len(t)
    for i in range(min(len_s, len_t)):
        if s[i] != t[i]:
            return ord(s[i]) - ord(t[i])
    return len_s - len_t


def qsort(L, left, right):
    """
    Lexicographically sort a list of words.

    :param list[str] L: list of words to sort
    :param int left: left list index
    :param int right: right list index
    """
    if left < right:
        q = left
        for i in range(left, right):
            if L[i] < L[right]:
                L[i], L[q] = L[q], L[i]
                q += 1
        L[q], L[right] = L[right], L[q]
        qsort(L, left, q-1)
        qsort(L, q+1, right)


def main():
    L = ["3.1.1", "0.0.1", "3.1.11", "0.0.2", "1.22.0"]
    qsort(L, 0, len(L)-1)
    print(L)


if __name__ == "__main__":
    main()
