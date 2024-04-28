def solution(sequence, k):
    answer = []
    interval_sum = 0
    end = 0
    n = len(sequence)
    # start를 차례대로 증가시키며 반복
    for start in range(n):
        # end를 가능한 만큼 이동시키기
        while interval_sum < k and end < n:
            interval_sum += sequence[end]
            end += 1
        # 부분합이 m일 때 카운트 증가
        if interval_sum == k:
            answer.append([start,end-1,end-1-start])
        interval_sum -= sequence[start]
        
    answer.sort(key = lambda x:x[2])
    return answer[0][0:2]

print("hi")