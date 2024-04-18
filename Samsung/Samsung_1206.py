T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    buildings = list(input().split())
    answer = 0
    if n == 4:
        answer = 0
    else: 
        for i in range(2,len(buildings)-2):
            b = int(buildings[i])
            left = buildings[i-2:i]
            right = buildings[i+1:i+3]
            left = [int(item) for item in left]
            right = [int(item) for item in right]
            max_value = max(max(left),max(right))

            if max_value < b:
                answer += b-max_value
    
    print(f"#{test_case} {answer}")

    