# script which solves the house robber problem with input as list
# [1,2,3,1] should return 4

def house_robber(houses: list):
    if houses == []:
        return 0
    answer = []
    for i, value in enumerate(houses):
        if i == 0:
            answer.append(value)
        elif i == 1:
            answer.append(max(answer[i-1], value))
        else:
            answer.append(max(value + answer[i-2], answer[i-1]))
    return max(answer)
