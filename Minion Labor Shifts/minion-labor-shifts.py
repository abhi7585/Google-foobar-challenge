def solution(data, n):
    temp = []
    for i in range(len(data)):
        if data.count(data[i]) <= n:
            temp.append(data[i])
    return temp


print(solution([5, 10, 15, 10, 7], 1))
