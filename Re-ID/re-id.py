def isprime(num):
    flag = True
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = False
                return False
                break
        if flag == True:
            return True

def solution(n):
    prime = []
    i = 2
    result = []
    while(len(prime) != n + 5):
        if isprime(i) == True:
            prime.append(i)
        i += 1
    j = n
    for i in range(5):
        result.append(prime[j])
        j += 1
    result = ''.join(map(str, result))
    if len(result) > 5:
        result = list(result)
        for i in range(len(result)-5):
            result.pop()
        return ''.join(result)
    else:
        return result
