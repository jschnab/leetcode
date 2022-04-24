"""
Given an integer array A, where A[i] = [winner_i, loser_i], indicating that
the player winner_i defeated loser_i in a game.

Return a list of size 2 where:

* the first element is the list of players that never lost
* the second element is the list of players who lost exactly one game

The result lists should be sorted by increasing order.
"""


def find_winners(A):
    """
    We count the number of games won and lost by each player, then list
    players with stats that match the question constraints.


    """
    players = {}  # players[x] = (wins, losses)
    for win, loss in A:
        # update winning stats
        tmp = players.get(win, [0, 0])
        tmp[0] += 1
        players[win] = tmp

        # update losing stats
        tmp = players.get(loss, [0, 0])
        tmp[1] += 1
        players[loss] = tmp

    winners = []
    losers = []
    for p, (win, loss) in players.items():
        if loss == 0:
            winners.append(p)
        elif loss == 1:
            losers.append(p)
    result = [sorted(winners), sorted(losers)]
    return result


def test1():
    games = [
        [1, 3],
        [2, 3],
        [3, 6],
        [5, 6],
        [5, 7],
        [4, 5],
        [4, 8],
        [4, 9],
        [10, 4],
        [10, 9],
    ]
    assert find_winners(games) == [[1, 2, 10], [4, 5, 7, 8]]
    print("test 1 successful")


def test2():
    games = [[2, 3], [1, 3], [5, 4], [6, 4]]
    assert find_winners(games) == [[1, 2, 5, 6], []]
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
