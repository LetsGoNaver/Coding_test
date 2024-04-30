def solution(plans):
    answer = []
    
    # 시간을 다 숫자로 바꾸기. 분으로 바꾸자
    total_time = 0
    start_times = {}
    
    plans.sort(key = lambda x:x[1])
    for inx,p in enumerate(plans):
        p[1] = int(p[1][0:2])*60 + int(p[1][3:5])
        p[2] = int(p[2])
        total_time += p[2]
        start_times[p[1]] = inx
    
    timmer = [0]*len(plans)
    start = plans[0][1]
    end = plans[-1][1]
    ready_q = []
    operating = []
    for t in range(start,end+total_time+1): # 처음에는 start,start+total_times 로 했는데 이러면 엄청 나중에 작업이 필요한게 무시됨. 충분히 길게 시간을 잡아줘야함.
        if operating:
            inx = operating[0]
            timmer[inx] += 1
            if timmer[inx] == plans[inx][2]:
                answer.append(plans[inx][0])
                operating.pop()
        if t in start_times.keys(): #시작시간이 된 과제를 만났을때
            inx = start_times[t]
            if operating:
                to_wait = operating.pop()
                ready_q.append(to_wait)
            operating.append(inx)
        else: #시작해야할 과제가 없는 경우 -> 실행중인거 하고, 실행중인게 없다면 기다리고 있는 프로세스 실행
            if operating:
                continue
            else:
                if ready_q:
                    inx = ready_q.pop()
                    operating.append(inx)
        
    return answer