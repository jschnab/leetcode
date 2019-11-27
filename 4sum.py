# leetcode problem 454 : 4sum II
# for 4 lists of integers A, B, C, D
# return the number of tuples (i, j, k, l)
# where A[i] + B[j] + C[k] + D[l] = 0

from collections import Counter

def 4sum(A, B, C, D):
    """Return the number of tuples (i, j, k, l)
    such that sum(A[i], B[j], C[k], D[l]) = 0"""

    AB = Counter(a + b for a in A for b in B)
    return sum(AB[-c-d] for c in C for d in D)
