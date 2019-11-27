# script which identifies if two strings representing rational numbers
# are equal
# return true for "0.(52)" and "0.5(25)"
# return true for "0.99(9)" and "1."

from fractions import Fraction

def equal_rational(S, T):
    """Return true if S and T are the same number else false."""

    def convert(S):
        """Convert number to Fraction object."""
        # if S is an integer
        if '.' not in S:
            return Fraction(int(S), 1)

        # get non-decimal part
        i = S.index('.')
        ans = Fraction(int(S[:i]), 1)

        # get decimal part
        S = S[i+1:]

        # if the repetition is not between brackets
        if '(' not in S:
            if S:
                ans += Fraction(int(S), 10 ** len(S))
            return ans

        # if there is a repetition between brackets
        i = S.index('(')
        if i:
            ans += Fraction(int(S[:i]), 10 ** i)
        S = S[i+1:-1]
        j = len(S)
        ans += Fraction(int(S), 10 ** i * (10 ** j - 1))
        return ans

    return convert(S) == convert(T)
