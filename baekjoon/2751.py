import sys
n = int(sys.stdin.readline())
result = []

for k in range(0, n):
    num = int(sys.stdin.readline())
    result.append(num)

result.sort()

for r in result:
    print(r)
