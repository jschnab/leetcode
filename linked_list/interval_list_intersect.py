# determine list of intersections of intervals
# given two lists of pairwise disjoint and sorted intervals

class Interval(object):
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end

    def interval_to_list(self):
        """Converts interval to list."""
        return [self.start, self.end]

class Solution(object):
    def interval_intersect(A, B):
        """Return list of intervals intersections."""
        # time complexity O(M+N)
        # where M and N are len(A) and len(B)
        # space complexity is O(M+N)

        # list of intervals
        answer = []
        
        # iterate through lists of intervals
        i = j = 0
        while i < len(A) and j < len(B):

            # determine if intervals intersect
            lo = max(A[i].start, B[j].start)
            hi = min(A[i].end, B[j].end)
            if lo <= hi:
                answer.append(Interval(lo, hi))

            if A[i].end < B[j].end:
                i += 1
            else:
                j += 1

        return answer

if __name__ == '__main__':

    # get list of intervals for A and B
    A = []
    n_A = int(input('How many intervals in A?'))
    for i in range(n_A):
        A.append(Interval(*map(int, input('Interval A[{0}] :'.format(i)).split())))
    B = []
    n_B = int(input('How many intervals in B?'))
    for i in range(n_B):
        B.append(Interval(*map(int, input('Interval B[{0}] :'.format(i)).split())))

    # get intervals intersections
    # A = [[0,2], [5,10], [13,23],[24,25]] B = [[1,5], [8,12], [15,24], [25,26]]
    # solution = [[1,2], [5,5], [8,10], [15,23], [24,24], [25,25]]
    answer = [i.interval_to_list() for i in Solution.interval_intersect(A, B)]
    print(answer)
