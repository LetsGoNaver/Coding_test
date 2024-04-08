T = int(input())
for test_case in range(1,T+1):
    numbers,n = input().split()
    n = int(n)
    answer = ""
    numbers = list(numbers)
    
    for i in range(n):
        if i >= len(numbers)-1:
            break
        start = numbers[i]
        leftover = numbers[i+1:]
        v = max(leftover)
        if start >= v:
            break #반드시 횟수 만큼 교환이 이루어져야함
        inx = len(leftover)-1
        while inx >= 0:
            if leftover[inx] == v:
                break
            else:
                inx -= 1
        temp = numbers[i]
        numbers[i] = numbers[inx+i+1]
        numbers[inx+i+1] = temp
    
    for s in numbers:
        answer += s

    print(f"#{test_case} {answer}")
