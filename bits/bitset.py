"""
leetcode #2166
Implement a bitset data structure.
"""


class Bitset1:
    """
    This class stores a list of bits.

    In addition to a list of bits, we maintain its inverse and
    the encoded value to improve the performance of some operations.

    Note: The most significant bits have the highest index in the list.
    """

    def __init__(self, size):
        """
        :param int size: Number of bits.
        """
        self._bits = [0] * size
        self._inv = [1] * size  # maintain inverse of self._bits
        self._n = 0  # the number of "on" bits
        self._value = 0  # the value encoded by self._bits
        self._max = 2 ** size - 1  # the maximum value the bitset can encode

    def fix(self, idx):
        """
        Set the bit at the provided index to "on".

        Time complexity: O(1).

        :param int idx: Index of the bit to set "on".
        """
        if not self._bits[idx]:
            self._n += 1
            self._value += 2 ** (len(self._bits) - idx - 1)
            self._bits[idx] = 1
            self._inv[idx] = 0

    def unfix(self, idx):
        """
        Set the bit at the provided index to "off".

        Time complexity: O(1).

        :param int idx: Index of the bit to set "off".
        """
        if self._bits[idx]:
            self._n -= 1
            self._value -= 2 ** (len(self._bits) - idx - 1)
            self._bits[idx] = 0
            self._inv[idx] = 1

    def flip(self):
        """
        Flip all bits.

        Since we maintain the inverse of the bitset, we can just swap them the
        bitset and its inverse.

        Time complexity: O(1).
        """
        self._n = len(self._bits) - self._n
        self._bits, self._inv = self._inv, self._bits
        self._value = self._max - self._value

    def all(self):
        """
        Returns True if all bits are "on" else False.

        Since we maintain the current value of the bitset, we can simply check
        if it is equal to the maximum possible value of the bitset.

        Time complexity: O(1).

        :returns (bool): True if all bits are "on" else False.
        """
        return self._value == self._max

    def one(self):
        """
        Returns True if at least one bit is "on", else False.

        Since we maintain the current value of the bitset, we can simply check
        if it is equal to zero, in which case no bit is "on".

        Time complexity: O(1).

        :returns (bool): True if at least one bit is "on" else False.
        """
        return self._value != 0

    def count(self):
        """
        Returns the number of bits set to "on".

        Time complexity: O(1).

        :returns (int): Number of "on" bits.
        """
        return self._n

    def to_string(self):
        """
        Returns the string representation of the bits.

        Time complexity: O(n) with n number of bits.

        :returns (str): String representation of the bits.
        """
        return "".join(str(b) for b in self._bits)


class Bitset:
    """
    This class stores a decimal integer to represent the bitset.
    """

    def __init__(self, size):
        """
        :param int size: Number of bits.
        """
        self._n = 0  # the number of "on" bits
        self._value = 0  # the value encoded by the bitset
        self._size = size

    def fix(self, idx):
        """
        Set the bit at the provided index to "on".

        Since we check that the bit is "off" at the provided index,
        we flip its value to "on" using OR and "on".

        Time complexity: O(1).

        :param int idx: Index of the bit to set "on".
        """
        if self._value & (1 << idx) == 0:
            self._n += 1
            self._value |= 1 << idx

    def unfix(self, idx):
        """
        Set the bit at the provided index to "off".

        Since we check that the bit is "on" at the provided index,
        we flip its value to "off" using XOR and "on".

        Time complexity: O(1).

        :param int idx: Index of the bit to set "off".
        """
        if self._value & (1 << idx) == 1:
            self._n -= 1
            self._value ^= 1 << idx

    def flip(self):
        """
        Flip all bits.

        We flip all bits using an "on" mask that covers all bits and XOR.

        Time complexity: O(1).
        """
        self._n = self._size - self._n
        self._value ^= (1 << self._size) - 1

    def all(self):
        """
        Returns True if all bits are "on" else False.

        Since we maintain the current value of the bitset, we can simply check
        if it is equal to the maximum possible value of the bitset.

        Time complexity: O(1).

        :returns (bool): True if all bits are "on" else False.
        """
        return self._n == self._size

    def one(self):
        """
        Returns True if at least one bit is "on", else False.

        Since we maintain the current value of the bitset, we can simply check
        if it is equal to zero, in which case no bit is "on".

        Time complexity: O(1).

        :returns (bool): True if at least one bit is "on" else False.
        """
        return self._n != 0

    def count(self):
        """
        Returns the number of bits set to "on".

        Time complexity: O(1).

        :returns (int): Number of "on" bits.
        """
        return self._n

    def to_string(self):
        """
        Returns the string representation of the bits.

        We use the bin() Python builtin. Since the most significant bit should
        be on the right, we reverse the bitstring and pad it with zero to match
        the size of the bitset. bin() also prepends the bitstring with "0b" so
        we remove these two characters.

        Time complexity: O(n) where n is the size of the bitset.

        :returns (str): String representation of the bits.
        """
        s = bin(self._value)[2:]
        return s[::-1] + "0" * (self._size - len(s))
