import sys

tmp1, tmp2 = sys.stdin.readline().split()
n = int(tmp1)
k = int(tmp2)

temp = []
result = []
total = 0

for i in range(0, n):
    t = int(sys.stdin.readline())
    temp.append(t)

    if len(temp) >= k:
        tmp = temp[i-k+1:i+1]
        tmp.sort()
        total += tmp[int((k-1)/2)]

print(total)
