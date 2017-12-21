import sys
n = int(sys.stdin.readline())

for i in range(0, n):
    total = i
    str_i = str(i)
    for s in str_i:
        total += int(s)
    
    if total == n:
        print(i)
        break
if i == n-1:
    print(0)
