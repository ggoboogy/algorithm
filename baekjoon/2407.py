import sys
tmp_n, tmp_m = sys.stdin.readline().split()
n = int(tmp_n)
m = int(tmp_m)

tmp1 = 1
tmp2 = 1
tmp3 = 1
for i in range(1, n+1):
    tmp1 *= i

for j in range(1, n-m+1):
    tmp2 *= j

for k in range(1, m+1):
    tmp3 *= k

print(tmp1//(tmp2*tmp3))
