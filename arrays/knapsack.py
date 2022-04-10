"""
See rosettacode.org/wiki/Knapsack_problem/0-1#Dynamic_programming_solution
"""

from collections import namedtuple


Item = namedtuple("Item", ["value", "weight"])


def knapsack(items, max_weight):
    """
    Dynamic programming solution of 0-1 knapsack.

    We iteratively build a table that store the maximum value of knapsacks of
    increasing weights, then we can read the list of items from the table.

    :param list[namedtuple] items: Items to put in the knapsack.
    :param int max_weight: Maximum weight of items.
    :returns (list[namedtuple]): List of items that fit the knapsack.
    """
    table = [[0 for _ in range(max_weight + 1)] for _ in range(len(items) + 1)]
    for i, item in enumerate(items, start=1):
        for w in range(1, max_weight + 1):
            # the item does not fit
            if item.weight > w:
                table[i][w] = table[i - 1][w]
            else:
                # we check if including the current item increases the value of
                # the knapsack
                table[i][w] = max(
                    table[i - 1][w],
                    table[i - 1][w - item.weight] + item.value
                )
    result = []
    for i in range(len(items), 0, -1):
        if table[i][max_weight] != table[i - 1][max_weight]:
            result.append(items[i - 1])
            max_weight -= items[i - 1].weight
    return result


def test1():
    items = [Item(5, 6), Item(2, 3), Item(1, 1), Item(3, 4)]
    max_weight = 9
    solution = knapsack(items, max_weight)
    assert sum(i.value for i in solution) == 7
    assert sum(i.weight for i in solution) == 9
    print("test 1 successful")


def main():
    test1()


if __name__ == "__main__":
    main()
