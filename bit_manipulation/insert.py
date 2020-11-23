# given 2 32-bit numbers, N and M, and two bit positions, i and j,
# we write a method to insert M into N such that M starts at bit j
# and ends at bit i
# we can assume that the bits j through i have enough space to fit all of M

# N = 10000000000 (1024 in decimal)
# M = 10011 (19 in decimal)


def insert(M, N, i, j):
    print(f"{bin(M):>16}")
    print(f"{bin(N):>16}")
    print(f"{bin(N | (M << i)):>16}")


def test1():
    insert(19, 1024, 2, 6)


def main():
    test1()


if __name__ == "__main__":
    main()
