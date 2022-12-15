def find_parent(x, parents):
    if parents[x] != x:
        parents[x] = find_parent(parents[x], parents)
    return parents[x]


def union(x, y, parents, ranks):
    px = find_parent(x, parents)
    py = find_parent(y, parents)
    if ranks[x] < ranks[y]:
        parents[x] = py
    else:
        parents[y] = px
        if ranks[x] == ranks[y]:
            ranks[y] += 1


def test1():
    n = 6
    graph = [(0, 2), (0, 3), (2, 3), (4, 5)]
    parents = list(range(n))
    ranks = [1] * n
    for x, y in graph:
        union(x, y, parents, ranks)
    for i in range(n):
        print(f"{i}: {parents[i]}")
    print()
    print("ranks:", ranks)


def main():
    test1()


if __name__ == "__main__":
    main()
