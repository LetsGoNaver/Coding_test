def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
        
def solution(n, k):
    answer = 0
    num = ""
    while True:
        if n < k:
            num = str(n) + num
            break
        elif n%k!=0:
            num = str(n%k) + num
            n = n//k
        else:
            num = "0" + num
            n = n//k

    target = ""
    arr = []
    for i in num:
        if i != "0":
            target += i
        elif i == "0" and target != "":
            arr.append(int(target))
            target =""
        else:
            continue
    if target!="":
        arr.append(int(target))
    for i in arr:
        if isPrime(i):
            answer +=1
        else:
            continue
    return answer