def solution(participant, completion):
    participant_dict = {}

    for person in participant:
        if person in participant_dict:
            participant_dict[person] += 1
        else:
            participant_dict[person] = 1

    for person in completion:
        if person in participant_dict:
            participant_dict[person] -= 1
            if participant_dict[person] == 0:
                del participant_dict[person]

    answer = list(participant_dict.keys())[0]
    return answer