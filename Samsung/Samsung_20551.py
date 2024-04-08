def compare(a,b,answer):
    if answer == -1:
        return answer,a
    
    if b == 1:
        answer = -1
        return answer,a
    
    while b <= a:
        a -= 1
        answer += 1

    return answer,a

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answer = 0
    one,two,three = map(int,input().split())

    # 2번 값을 줘야해 
    if two < three:
        answer,one = compare(one,two,answer)
    else:
        answer,two = compare(two,three,answer)
        answer,one = compare(one,two,answer)
    
    print(f"#{test_case} {answer}")