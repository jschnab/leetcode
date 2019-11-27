# script which takes as input as list of integers and a target integer
# and finds if two integers from the list add up to the target
# return the index of two such integers

# iterate through list and add to dictionary to quickly check
# if two numbers can add to the target

def two_sum(mylist, target):
    """Return the index of two integers which add up to the target."""
    dic = {}
    for i, n in enumerate(mylist):
        dic[n] = i
        complement = target - n
        if complement in dic and dic[complement] != i:
            return [i, dic[complement]]

if __name__ == '__main__':
    mylist = list(map(int, input().split()))
    target = int(input())
    two_sum(mylist, target)
