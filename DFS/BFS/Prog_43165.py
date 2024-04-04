from itertools import combinations

def solution(numbers, target):
    answer = 0
    
    for i in range(1,len(numbers)):
        for c in combinations(numbers,i):
            total = sum(numbers) - sum(c)*2
            if total == target:
                answer += 1
    
        
    return answer


# 아래는 DFS로 된 풀이 - 재귀를 이용한다

def DFS(idx, numbers, target, value):
    global answer
    N = len(numbers)
    if(idx== N and target == value):
        answer += 1
        return
    if(idx == N):
        return

    DFS(idx+1,numbers,target,value+numbers[idx])
    DFS(idx+1,numbers,target,value-numbers[idx])
    
def solution(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    return answer