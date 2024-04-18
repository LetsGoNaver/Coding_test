def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        criteria = prices[i]
        count = 0
        for j in range(i+1,len(prices)):
            if criteria <= prices[j]:
                count += 1
            else:
                count += 1
                break
        answer.append(count)
    answer.append(0)
    return answer