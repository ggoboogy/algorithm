def solution(v):
    answer = []
    for i in range(0,2):
        if v[0][i] == v[1][i]:
            answer.append(v[2][i])
        elif v[1][i] == v[2][i]:
            answer.append(v[0][i])
        else:
            answer.append(v[1][i])
    print(answer)
    return answer
