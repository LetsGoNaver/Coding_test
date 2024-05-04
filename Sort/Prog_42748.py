def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        new_arr = array[i-1:j]
        new_arr.sort()
        answer.append(new_arr[k-1])
    return answer