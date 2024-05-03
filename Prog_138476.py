from collections import Counter

def solution(k, tangerine):
    answer =0 
    cnt = Counter(tangerine)
    cnt = list(cnt.most_common())
    for i in cnt:
        k = k - i[1]
        answer +=1
        if k <=0:
            break
    return answer 