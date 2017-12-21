import sys

n = int(sys.stdin.readline())
result = 1

for i in range(1, n+1):
    result *= i

cnt = 0
result = str(result)
length = len(result)
for i in range(0, length):
    if result[length-i-1] != '0':
        break
    else:
        cnt+=1

print(cnt)
