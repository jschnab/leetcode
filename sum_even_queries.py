# return the sum of even numbers in a list of integers A
# after A is permanently updated according to a list of queries [value, index]
# for each query, the value is added to A[index]

class Solution(object):
    def sum_even_queries(A, queries):

        answer = []

        # sum of even numbers in A
        S = sum(x for x in A if not x & 1)

        for value, index in queries:

            # if A[index] is even, the sum will change
            if not A[index] & 1:
                S -= A[index]

            # we update A anyway
            A[index] += value

            # we update the sum if A[index] is even
            if not A[index] & 1:
                S += A[index]

            answer.append(S)

        return answer

if __name__ == '__main__':

    # input A and queries
    A = list(map(int, input('Please enter A elements: ').split()))
    queries = []
    q = len(A)
    for i in range(q):
        queries.append(list(map(int, input('Query {0} :'.format(i)).split())))
    
    # calculate solution
    # A = [1, 2, 3, 4] queries = [[1,0], [-3,1], [-4,0], [2,3]]
    # answer = [8, 6, 2, 4]

    print(Solution.sum_even_queries(A, queries))
