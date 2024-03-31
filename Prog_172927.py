def solution(picks, minerals):
    five_minerals = []
    answer = 0

    minerals = minerals[0:sum(picks)*5]

    for i in range(0,len(minerals),5):
        five_minerals.append(minerals[i:i+5])

    five_minerals.sort(key=lambda x: (x.count('diamond'), x.count('iron')), reverse=True)

    for i in five_minerals:
        dia = i.count("diamond")
        iron = i.count("iron")
        stone = i.count("stone")
        if picks[0] > 0:
            answer += dia + iron + stone
            picks[0] -= 1
        elif picks[1] > 0:
            answer += dia*5 + iron + stone
            picks[1] -= 1
        elif picks[2] > 0:
            answer += dia*25 + iron*5 + stone
            picks[2] -= 1

    return answer