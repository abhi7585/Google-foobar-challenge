def solution(l, t):
    result = [[]]
    index = []
    flag = False
    for i in range(len(l) + 1):
        for j in range(i+1, len(l) + 1):
            result.append(l[i:j])
            index.append([i, j-1])
    result.pop(0)
    for i in range(len(result)):
        temp = result[i]
        if sum(temp) == t:
            flag = True
            return index[i]
    if flag == False:
        return [-1, -1]
