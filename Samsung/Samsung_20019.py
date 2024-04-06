T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
from collections import deque
def palin(string):
    # 회문안 회문의 문자 앞뒤는 순서를 바꿔서 같아야함
    n = len(string)
    n -= 1
    half = int(n/2)
    f = deque(list(string[0:half])) # 이거는 앞부터 빼니까 큐
    s = list(string[half+1:]) # 이거는 뒤부터 빼니까 스택
    while f:
        if f.popleft() == s.pop():
            continue
        else:
            return False
    
    return True
    
for test_case in range(1, T + 1):
    answer = ""
    # 토마토
    string = input()
    n = len(string)
    if n == 5:
        answer = "NO"
    elif n%2 == 0:
        answer = "NO"
    else:
        n -= 1
        half = int(n/2)
        f = string[0:half]
        s = string[half+1:]
        
        if palin(string):
            if palin(f):
                answer = "YES"
            else: 
                answer = "NO"
        else:
            answer = "NO"
    
    print(f"#{test_case} {answer}")
    