import sys
tmp_a, tmp_b = sys.stdin.readline().split()
a = int(tmp_a)
b = int(tmp_b)

max_num = max(a, b)
curr_num = max_num
while curr_num <= a*b:
    if curr_num % min(a,b) == 0:
        break
    
    curr_num += max_num

print(curr_num)
