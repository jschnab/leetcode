"""
leetcode 2456: most populat video creator

We are given two string arrays 'creators' and 'ids', and an integer array
'views', all of length n. The ith video on a platform was created by
creators[i], has an ID of ids[i], and has views[i] views.

The popularity of a creator is the sum of the number of views on all the
creator's videos. Find the creator with the highest popularity and the id of
their most viewed video.

If several creators have the highest popularity, find all of them.

If multiple videos have the highest view count for a creator, find the
lexicographically smallest ID.

Return a 2D array of strings 'answer' where answer[i] = [creator, id] means
that creator has the highest popularity and id is the ID of their most popular
video. The answer can be returned in any order.
"""


def popular(creators, ids, views):
    creators_pop = {}
    for i in range(len(creators)):
        if creators[i] not in creators_pop:
            creators_pop[creators[i]] = {
                "pop_tot": views[i],
                "pop_vid": [ids[i]],
                "most_pop": views[i],
            }
        else:
            creators_pop[creators[i]]["pop_tot"] += views[i]
            if creators_pop[creators[i]]["most_pop"] == views[i]:
                creators_pop[creators[i]]["pop_vid"].append(ids[i])
            elif creators_pop[creators[i]]["most_pop"] < views[i]:
                creators_pop[creators[i]]["pop_vid"] = [ids[i]]
                creators_pop[creators[i]]["most_pop"] = views[i]

    creators_sorted = sorted(
        creators_pop.items(), key=lambda x: x[1]["pop_tot"], reverse=True,
    )

    highest_pop = creators_sorted[0][1]["pop_tot"]
    creators_sorted[0][1]["pop_vid"].sort()
    idx = 1
    if len(creators_sorted) > 1:
        while (
            idx < len(creators_sorted)
            and creators_sorted[idx][1]["most_pop"] == highest_pop
        ):
            creators_sorted[idx][1]["pop_vid"].sort()
            idx += 1

    return [
        [creators_sorted[i][0], creators_sorted[i][1]["pop_vid"][0]]
        for i in range(idx)
    ]


def test1():
    creators = ["alice", "bob", "alice", "chris"]
    ids = ["one", "two", "three", "four"]
    views = [5, 10, 5, 4]
    expected = [["alice", "one"], ["bob", "two"]]
    assert popular(creators, ids, views) == expected
    print("test 1 successful")


def test2():
    creators = ["alice", "alice", "alice"]
    ids = ["a", "b", "c"]
    views = [1, 2, 2]
    expected = [["alice", "b"]]
    assert popular(creators, ids, views) == expected
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
