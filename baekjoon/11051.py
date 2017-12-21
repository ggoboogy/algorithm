import sys
tmp_n, tmp_k = sys.stdin.readline().split()

n = int(tmp_n)
k = int(tmp_k)

num = [1 for i in range(0, n+1)]

for i in range(2, n+1):
    num[i] = num[i-1]*i

print((num[n]//(num[k]*num[n-k]))%10007)
