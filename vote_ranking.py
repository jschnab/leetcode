# ranking by votes
# leetcode 1366

# a group of teams identified by uppercase letters is ranked
# through a positional voting system, e.g. for 3 teams A, B and C
# voter 1: ABC, voter 2: BAC, etc
# the winning team has received the most position 1 votes
# if there are ties at any given position, we consider the next position
# if there are still ties after all votes are considered, ranking is done by
# alphabetical order

# example, given an array of votes:
# ["ABC", "ACB", "ABC", "ACB", "ACB"]
# return "ACB"

from collections import Counter


def ranking_votes(votes):
    # we add [v] in case all voters vote the same
    count = {v: [0] * len(votes[0]) + [v] for v in votes[0]}
    for vote in votes:
        for i, v in enumerate(vote):
            count[v][i] -= 1
    return "".join(sorted(votes[0], key=count.get))
