import bisect

def solution(book_time):
    rooms_dict = {0:[]}
    book_time.sort(key = lambda x:x[0])
    # 시간을 다 그냥 분으로 바꿔
    for inx,time in enumerate(book_time):
        start = int(time[0][0:2])*60 + int(time[0][3:])
        end = int(time[1][0:2])*60 + int(time[1][3:]) + 10
        
        if inx == 0:
            rooms_dict[0].append(start)
            rooms_dict[0].append(end)
        else:
            inserted = False
            for key in rooms_dict.keys():
                s = bisect.bisect_right(rooms_dict[key],start)
                e = bisect.bisect_left(rooms_dict[key],end)
                if s == e and s==len(rooms_dict[key]):
                    rooms_dict[key].insert(s,end)
                    rooms_dict[key].insert(e,start)
                    inserted = True
                    break
            
            if not inserted:
                end_num = list(rooms_dict.keys())[-1] + 1
                rooms_dict[end_num] = [start,end] 
                            
    return len(rooms_dict.keys())
