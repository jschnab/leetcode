"""
leetcode 2241: design an ATM machine.

Our ATM machine stores bank notes of 5 denomiations: 20, 50, 100, 200 and 500
euros. Initially the ATM is empty. The user can deposit or withdraw any amount
of money.

When withdrawing, the machine prioritizes banknotes of larger values. For
example, to withdraw 300, if there are 2 x 50 bank notes, 1 x 100, and 1 x 200
then the machine will use the 200 and 100 bank notes. To withdraw 600, if there
are 3 x 200 and 1 x 500 then the request will be rejected because as the
machine prioritizes larger notes, it will try to use the 500 and then be unable
to complete the remaining 100. The machine is unable to skip 500 and go
directly to 200.

Implement an ATM class with the following methods:

* deposit(list[int]) which takes a list of bank notes counts in order of
increasing value and deposits them, and returns nothing.
* withdraw(int) which takes an amount to withdraw, returns a list of bank note
counts (increasing value order) and update the count of notes in the machine.
It returns [-1] if it is not possible to withdraw for any reason.
"""


class ATM:

    def __init__(self):
        self.values = [20, 50, 100, 200, 500]
        self.notes = [0] * 5

    def deposit(self, counts):
        self.notes = [x + y for x, y in zip(self.notes, counts)]

    def withdraw(self, amount):
        result = [0] * len(self.notes)
        for i in reversed(range(len(result))):
            result[i] = min(self.notes[i], amount // self.values[i])
            amount -= result[i] * self.values[i]
        if amount == 0:
            self.notes = [x - y for x, y in zip(self.notes, result)]
            return result
        return [-1]
