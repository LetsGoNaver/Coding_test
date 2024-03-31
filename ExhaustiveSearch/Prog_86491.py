def solution(sizes):
    answer =0
    fisrt_max=0
    second_max=0
    for i in sizes:
        i.sort()
        
        if fisrt_max < i[0]:
            fisrt_max = i[0]

        if second_max < i[1]:
            second_max = i[1]

    answer = fisrt_max * second_max
        
    return answer