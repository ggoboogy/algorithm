def solution(arr):
    sum = 0
    correct_sum = 0
    answer = True
    for i in range(1, len(arr)+1):
        sum ^= arr[i-1]
        correct_sum ^= i
    
    if sum == correct_sum:
        answer = True
    else:
        answer = False
        
    return answer
