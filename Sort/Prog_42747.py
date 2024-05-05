def solution(citations):
    h = max(citations)
    max_ = 0
    for i in range(h): # 인용수 최댓값까지 h 찾아보기
        higher_i = 0
        lower_i = 0
        for cite in citations: # 조건 확인하기
            if cite >= i:
                higher_i += 1
            else:
                lower_i += 1
        if higher_i >= i:
            if i > max_:
                max_ = i
    return max_