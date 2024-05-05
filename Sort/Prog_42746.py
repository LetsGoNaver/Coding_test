def solution(numbers):
    numbers = list(map(str, numbers))

    # 4자리수로 반환해서 정렬
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    answer = ''.join(numbers)

    # 0이 여러개일 경우, "000" 대신 "0"을 반환하도록 예외처리
    if answer[0] == '0':
        return '0'
    else:
        return answer