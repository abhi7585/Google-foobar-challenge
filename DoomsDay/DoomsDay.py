def solution(area):
    result = []
    temp = area
    if area == 1:
        return [1]
    else:
        while area != 0:
            for i in range(temp):
                if i * i > area:
                    result.append((i-1) ** 2)
                    area -= (i-1) ** 2
                    break
        return result
