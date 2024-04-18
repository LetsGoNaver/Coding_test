n = int(input())

for _ in range(n):
    t_arr = [] # 필요 요일수
    p_arr = [] # 수익
    t,p = map(int,input().split())
    t_arr.append(t)
    p_arr.append(p)
    answer = 0
    for i in range(n):
        profit = 0
        if i == n-1:
            if t_arr[i] != 1:
                break
            else:
                if answer < p_arr[i]:
                    answer = p_arr[i]
        else:
            for j in range(i,n):
                pass




        # if answer < profit:
        #     answer = profit

