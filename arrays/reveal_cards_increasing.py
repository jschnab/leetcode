# leetcode challenge 950: reveal cards in increasing order
# we're given a deck of cards where every card is a unique integer
# initially all cards are face down
# we do the following steps:
# * take top card, reveal it, and discard it
# * if there are still cards left, put the top card at the bottom of the deck
# * go back to step 1
# return and ordering of the deck that reveals the cards in increasing order


from collections import deque


class ListNode:
    def __init__(self, val=None, prev=None, next_=None):
        self.val = val
        self.prev = prev
        self.next = next_


def reveal(array):
    array_sorted = sorted(array)
    head = ListNode(array_sorted[-1])
    first = last = head

    # iterate through sorted array from end to beginning
    for i in reversed(range(len(array)-1)):
        if i < len(array) - 2:
            # put last node first
            last.next = first
            first.prev = last
            first = first.prev
            last = last.prev
            last.next = None
            first.prev = None

        # add new node at beginning of list
        new = ListNode(array_sorted[i], next_=first)
        first.prev = new
        first = new

    # convert linked list to array
    result = []
    while first:
        result.append(first.val)
        first = first.next
    return result


def reveal2(deck):
    q = deque()
    deck.sort()
    for i in reversed(range(len(deck))):
        if i < len(deck) - 2:
            q.appendleft(q.pop())
        q.appendleft(deck[i])
    return list(q)


def test1():
    array = [17, 13, 11, 2, 3, 5, 7]
    result = reveal2(array)
    assert result == [2, 13, 3, 11, 5, 17, 7]
    print("test 1 successful")


def test2():
    array = [1]
    result = reveal2(array)
    assert result == [1]
    print("test 2 successful")


def main():
    test1()
    test2()


if __name__ == "__main__":
    main()
