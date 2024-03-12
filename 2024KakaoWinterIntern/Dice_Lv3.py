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

    


# GPT 의 정답 - 내 코드는 시간 복잡도에서 문제가 생겼다 

from itertools import combinations, product
from collections import defaultdict

def calculate_distribution(dice):
    dist = defaultdict(int)
    for value in dice:
        dist[value] += 1
    return dist

def combine_distributions(dist1, dist2):
    combined = defaultdict(int)
    for val1, count1 in dist1.items():
        for val2, count2 in dist2.items():
            combined[val1 + val2] += count1 * count2
    return combined

def solution(dice):
    n = len(dice)
    half_n = n // 2
    max_win_probability = -1
    best_combination = []

    # 각 주사위의 점수 분포를 계산
    distributions = [calculate_distribution(d) for d in dice]

    # 모든 가능한 주사위 조합을 생성
    for dice_a in combinations(range(n), half_n):
        dist_a = defaultdict(int, {0: 1})
        dist_b = defaultdict(int, {0: 1})

        for d in dice_a:
            dist_a = combine_distributions(dist_a, distributions[d])
        for d in set(range(n)) - set(dice_a):
            dist_b = combine_distributions(dist_b, distributions[d])

        # 승리 확률 계산
        total_cases = sum(dist_a.values()) * sum(dist_b.values())
        wins = sum(count_a * sum(count_b for key_b, count_b in dist_b.items() if key_b < key_a)
                   for key_a, count_a in dist_a.items())

        win_probability = wins / total_cases

        if win_probability > max_win_probability:
            max_win_probability = win_probability
            best_combination = dice_a

    # 주사위 번호에 1을 더함
    return [x + 1 for x in sorted(best_combination)]