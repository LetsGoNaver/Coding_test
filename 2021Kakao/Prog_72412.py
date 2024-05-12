from itertools import combinations
from collections import defaultdict
import bisect

def solution(info, query):
    answer = []
    db = defaultdict(list)

    for i in info:  # 정보 저장
        temp = i.split()
        conditions = temp[:-1]  # 조건들만 모아둠
        score = int(temp[-1])  # 점수 따로 저장
        for n in range(5):  # 조건들에 대해 조합을 이용해서  
            combi = list(combinations(range(4), n))
            for c in combi:
                temp_c = conditions.copy()
                for v in c:  # '-'를 포함한 조건 생성
                    temp_c[v] = '-'
                changed_t = '/'.join(temp_c)
                db[changed_t].append(score)

    for value in db.values():  # 이진탐색을 위해 점수 오름차순으로 정렬
        value.sort()

    for q in query:  # 쿼리 조건에 맞는 값 찾기
        qry = [i for i in q.split() if i != 'and']
        qry_cnd = '/'.join(qry[:-1])
        qry_score = int(qry[-1])
        if qry_cnd in db:  # 쿼리 조건에 해당하는 값들에 대해서
            data = db[qry_cnd]
            enter = bisect.bisect_left(data, qry_score)  # 이진탐색
            answer.append(len(data) - enter)
        else:
            answer.append(0)

    return answer