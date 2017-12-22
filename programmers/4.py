def solution(board):
    if len(board) == 0:
        return 0
    
    y = len(board)
    x = len(board[0])
    sum_arr = []
    
    for i in range(0, x):
        sum_arr.append(0)
        
    answer = 0
    for i in range(0, y):
        for k in range(0, x):
            if board[i][k] == 1: sum_arr[k] += 1
            else: sum_arr[k] = 0
        
        max_val = max(sum_arr)
        while max_val >= 1 and max_val > answer:
            cnt = 0
            for k in range(0, x):    
                if sum_arr[k] >= max_val: cnt += 1
                else: cnt = 0
            
                if cnt == max_val: break
            
            if cnt == max_val and max_val > answer:
                answer = max_val
                break
            else:
                max_val -= 1
    
    answer *= answer
    return answer
