def solution(bandage, health, attacks):
    time = 1
    success_time = 1
    end_time = attacks[-1][0]
    
    attack_dic = dict()
    
    h = health
    
    for a in attacks:
        attack_dic[a[0]] = a[1]
        
    while time <= end_time:
        if time in attack_dic.keys():
            h -= attack_dic[time]
            success_time = 0
            success_time += 1
            time += 1
            if h <= 0:
                h = -1
                break
        elif h == health:
            success_time += 1
            time += 1
            continue
        elif success_time == bandage[0]:
            h += bandage[2]
            h += bandage[1]
            if h > health:
                h = health
            success_time = 0
            success_time += 1
            time += 1
        else:
            h += bandage[1]
            if h > health:
                h = health
            success_time += 1
            time += 1
        print(h)
        
    answer = h
    return answer