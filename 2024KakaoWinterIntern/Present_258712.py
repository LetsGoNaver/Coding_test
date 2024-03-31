def solution(friends, gifts):
    answer = 0
    
    friends_dic = {}
    for friend in friends:
        friends_dic[friend] = [0,0,0] # send, receive, present num
    
    for gift_set in gifts:
        sender , receiver = gift_set.split()
        friends_dic[sender][0] += 1
        friends_dic[receiver][1] += 1
    
    table = []
    table.append(friends)
    table.append(friends)


    table_value = []
    for i in range(len(friends)):
        table_value.append([0] * len(friends))
    
    for pairs in gifts:
        A,B = pairs.split()
        index = table[0].index(A)
        col = table[1].index(B)
        table_value[index][col] += 1
    

    for index in range(0,len(friends)-1):
        for col in range(index+1,len(friends)):
            AtoB = table_value[index][col]
            BtoA = table_value[col][index]
            A = table[0][index]
            B = table[1][col]

            if AtoB > BtoA:
                friends_dic[A][2] +=1
            elif AtoB < BtoA:
                friends_dic[B][2] +=1 
            elif (AtoB == 0 and BtoA == 0) or AtoB == BtoA:
                A_index = friends_dic[A][0] - friends_dic[A][1]
                B_index = friends_dic[B][0] - friends_dic[B][1]
                if A_index > B_index:
                    friends_dic[A][2] +=1
                elif A_index < B_index:
                    friends_dic[B][2] +=1
                else:
                    pass
        
        
    max = 0
    for key in friends_dic.keys():
        temp = friends_dic[key][2]
        if max < temp:
            max = temp
        
    answer = max
    return answer


    
