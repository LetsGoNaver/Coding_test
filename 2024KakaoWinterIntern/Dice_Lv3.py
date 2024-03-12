from itertools import combinations,product

def solution(dice):
    result_list = []
    
    possible_sets = list(combinations(list(range(len(dice))),int(len(dice)/2)))
    
    for sets in possible_sets:
        A_dices = []
        B_dices = []
        
        for A_num in sets:
            A_dices.append(dice[A_num])
        
        for B_num in set(range(len(dice))):
            if B_num not in sets:
                B_dices.append(dice[B_num])
        
        temp = list(product(list(range(6)),repeat = int(len(dice)/2)))
        
        win = 0
        draw = 0
        lose = 0

        for i in temp:
            total_A = 0
            dice_index = 0
            for index in i:
                total_A += A_dices[dice_index][index]
                dice_index += 1
            
            for j in temp:
                total_B = 0
                dice_index = 0
                for index in j:
                    total_B += B_dices[dice_index][index]
                    dice_index += 1
            
                if total_A > total_B :
                    win += 1
                elif total_A == total_B:
                    draw += 1
                else:
                    lose += 1
                
        win_rate = win/(win+lose+draw)
        num_list = list(sets)
        
        result = []
        for i in num_list:
            i +=1
            result.append(i)
            
        result.sort()
        
        result.append(win_rate)
        result_list.append(result)
    
    result_list.sort(key = lambda x:x[1] , reverse = True)
    
    max = 0
    answer =[]
    for results in result_list:
        if results[-1] > max:
            max = results[-1]
            answer = results[:-1]
    
    return answer

    

        