import sys
import math

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

total = 0
start = int(math.sqrt(m))
flag = 0
min_value = 0
for i in range(start, int(math.sqrt(n))+1):
    if i*i >= m and i*i <= n:
        total += i*i
        if flag == 0:
            min_value = i*i
            flag = 1

if total == 0:
    print(-1)
else:
    print(total)
    print(min_value)
