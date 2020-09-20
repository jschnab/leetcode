# towers of hanoi


class Stack:
    def __init__(self, name="", items=None):
        self.name = name
        self.items = items or []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __str__(self):
        return str(self.items)


def move_disk(from_peg, to_peg):
    print(f"pop from {from_peg.name} and push to {to_peg.name}")
    to_peg.push(from_peg.pop())


def towers_hanoi(n_disks, from_peg, to_peg, spare_peg):
    """
    Solve the towers of hanoi problem: move n disks from a starting
    peg to a destination peg, using a spare peg.

    Time complexity: O(2^n)
    Space complexity: O(1)
    """
    if n_disks == 0:
        return
    towers_hanoi(n_disks - 1, from_peg, spare_peg, to_peg)
    move_disk(from_peg, to_peg)
    towers_hanoi(n_disks - 1, spare_peg, to_peg, from_peg)


def test1():
    items = list(range(1, 4))[::-1]
    A = Stack("A", items.copy())
    B = Stack("B")
    C = Stack("C")
    towers_hanoi(3, A, B, C)
    assert B.items == items and not A.items and not C.items
    print("test 1 successful")


def main():
    test1()


if __name__ == "__main__":
    main()
