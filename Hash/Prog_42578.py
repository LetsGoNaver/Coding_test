from itertools import combinations
def solution(clothes):
    answer = 0
    c_dic = dict()
    
    for c in clothes:
        if c[1] in c_dic.keys():
            c_dic[c[1]].append(c[0])
        else:
            c_dic[c[1]] = [c[0]]
            
    
    # for k in c_dic.keys():
    #     answer += len(c_dic[k]) # 종류에서 하나씩 고른 경우 더하기
    
    
    for r in range(1,len(c_dic.keys())+1):
        for combi in combinations(c_dic.keys(),r):
            n = 1
            for c in combi:
                n = n*len(c_dic[c])
            answer += n
            
    return answer