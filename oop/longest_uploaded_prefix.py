"""
leetcode 2424: longest uploaded prefix

We are given a stream of n videos, each representing a distinct number from 1
to n, that we need to upload to a server. We need to implement a data structure
that calculates the length of the longest uploaded prefix at various points in
the upload process.

We consider i to be an uploaded prefix if all videos in the range 1 to i
(inclusive) have been uploaded to the server. The longest uploaded prefix is
the maximum value of i that satisfies this definition.
"""


class LUPrefix:
    def __init__(self, n):
        self.uploaded = [False] * n
        self.idx = 0

    def upload(self, vid):
        self.uploaded[vid - 1] = True

    def longest(self):
        while self.idx < len(self.uploaded) and self.uploaded[self.idx]:
            self.idx += 1
        return self.idx


def test1():
    P = LUPrefix(4)
    P.upload(3)
    assert P.longest() == 0
    P.upload(1)
    assert P.longest() == 1
    P.upload(2)
    assert P.longest() == 3
    print("test 1 successful")


def main():
    test1()


if __name__ == "__main__":
    main()
