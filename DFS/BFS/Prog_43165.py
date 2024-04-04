from itertools import combinations

def solution(numbers, target):
    answer = 0
    
    for i in range(1,len(numbers)):
        for c in combinations(numbers,i):
            total = sum(numbers) - sum(c)*2
            if total == target:
                answer += 1
    
        
    return answer