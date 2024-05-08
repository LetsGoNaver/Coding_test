import math

def solution(fees,records):
    answer = []
    car_num = []
    for i in records:
        i = i.split()
        car_num.append(i[1])
    car_num = set(car_num)

    car_lists = {f'{i}': [] for i in car_num}
        
    for i in records:
        i = i.split()
        time = i[0]
        time = int(time[0:2]) * 60 + int(time[3:5])
        car_lists[i[1]].append(time)
    
    car_lists = {k: car_lists[k] for k in sorted(car_lists)}

    base_time = fees[0]
    base_price = fees[1]
    per_min = fees[2]
    per_price = fees[3]

    for i in car_lists:
        fee = 0
        total_time = 0
        if len(car_lists[i]) % 2 == 0:
            for j in range(0, len(car_lists[i]), 2):
                total_time += car_lists[i][j+1] - car_lists[i][j]
        else:
            for j in range(0, len(car_lists[i])-1, 2):
                total_time += car_lists[i][j+1] - car_lists[i][j]
            total_time += 23*60 + 59 - car_lists[i][-1]
            
        if total_time <= base_time:
            fee += base_price
        else:
            fee += base_price + math.ceil((total_time - base_time)/per_min) * per_price

        answer.append(fee)
    
    return answer