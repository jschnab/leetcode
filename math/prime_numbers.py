import math


def isprime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors


"""
leetcode 2507: smallest value after replacing with sum of prime factors

We are given a positive integer n.

Continuously replace n with the sum of its prime factors.

Note that if a prime factor divides n multiple times, it should be included in
the sum as many times as it divides n.

Return the smallest value n will take.
"""
def replace_sum_prime_factors(n):
    s = 0
    i = 2
    cur = n
    while i * i <= cur:
        while cur % i == 0:
            s += i
            cur //= i
        i += 1
    if cur > 1:
        s += cur
    if s == n:
        return s
    return replace_sum_prime_factors(s)


def test_replace_sum():
    test_cases = [
        {"in": 15, "out": 5},
        {"in": 3, "out": 3},
        {"in": 4, "out": 4},
        {"in": 6, "out": 5},
    ]
    for tc in test_cases:
        assert replace_sum_prime_factors(tc["in"]) == tc["out"]
    print("tests successful")


if __name__ == "__main__":
    test_replace_sum()
