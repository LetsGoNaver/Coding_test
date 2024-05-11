import itertools
from collections import Counter

def solution(orders, course):
    answer = []

    for num in course:
        all_combi = []
        for order in orders:
            # 주문에서 가능한 모든 조합을 생성한다
            combinations = itertools.combinations(sorted(order), num)
            for combi in combinations:
                all_combi.append(''.join(combi))

        # 생성된 모든 조합의 빈도를 계산한다
        counter = Counter(all_combi)

        # 빈도가 가장 높은 조합을 찾는다. 동일한 빈도수의 조합이 여러 개인 경우 모두 찾는다.
        max_count = 0
        max_combi = []
        for combi, count in counter.items():
            if count > max_count and count > 1:  # 빈도수가 1보다 큰 조합만 고려한다
                max_count = count
                max_combi = [combi]
            elif count == max_count:
                max_combi.append(combi)
        answer.extend(max_combi)

    return sorted(answer)  # 사전 순서로 정렬된 결과를 반환한다