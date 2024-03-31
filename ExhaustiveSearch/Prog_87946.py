from itertools import permutations
def solution(k, dungeons):
    answer = -1
    
    for p in permutations(range(len(dungeons))):
        count = 0
        health = k
        for n in p:
            req = dungeons[n][0]
            consume = dungeons[n][1]
            if health < req:
                continue
            else:
                health -= consume
                count += 1
        if answer < count:
            answer = count
    return answer