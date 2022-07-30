"""
leetcode 2284: sender with largest word count.

We have a chat log of n messages. We are given two string arrays messages and
senders, where message[i] is a message sent by senders[i]/

A message is a list of words separated by a single space with no leading or
trailing spaces.

Return the sender with the largest word count. If there is more than one sender
with the same largest word count, return the one with the lexicographically
largest name.

Uppercase letters come before lowercase letters in lexicographical order.
"""


def word_count(messages, senders):
    """
    Time complexity: O(nlogn) with n = number of senders because we sort
    senders.

    Space complexity: O(n) because we build a dictionary where keys are
    senders.

    :param list(str) messages: Messages.
    :param list(str) senders: Senders.
    :returns (str): Name of the sender with largest word count.
    """
    counts = {}
    for i in range(len(senders)):
        counts[senders[i]] = counts.get(senders[i], 0) + len(
            messages[i].split()
        )
    counts_sorted = sorted(counts.items(), key=lambda x: (x[1], x[0]))
    return counts_sorted[-1][0]


def test1():
    messages = [
        "Hello userTwooo",
        "Hi userThree",
        "Wonderful day Alice",
        "Nice day userThree",
    ]
    senders = ["Alice", "userTwo", "userThree", "Alice"]
    assert word_count(messages, senders) == "Alice"
    print("test 1 successful")


def test2():
    messages = [
        "How is leetcode for everyone",
        "Leetcode is useful for practice",
    ]
    senders = ["Bob", "Charlie"]
    assert word_count(messages, senders) == "Charlie"
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
