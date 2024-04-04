def solution(genres, plays):
    answer = []
    
    music_dic = dict()
    
    max = 0

    for inx,p in enumerate(plays):
        if genres[inx] not in music_dic.keys():
            music_dic[genres[inx]] = []
        music_dic[genres[inx]].append([inx,p])

    order = []
    for k in music_dic.keys():
        count = 0
        arr = music_dic[k]
        for n in arr:
            count += n[1]
        order.append([k,count])
        
    order.sort(reverse=True,key=lambda x : x[1])

    def pop2songs(key):
        arr = music_dic[key]
        arr.sort(reverse=True,key=lambda x : x[1])
        if len(arr) == 1:
            answer.append(arr[0][0])
        else:
            for i in range(2):
                answer.append(arr[i][0])
    
    for i in order:
        pop2songs(i[0])
    
    return answer