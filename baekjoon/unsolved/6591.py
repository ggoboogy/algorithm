import sys

result = []
while True:
    tmp_n, tmp_k = sys.stdin.readline().split()
    n = int(tmp_n)
    k = int(tmp_k)

    if n == 0 and k == 0: break

    boonmo = 1
    boonja = 1

    for i in range(2, n-k+1): boonmo *= i
    num = n
    for k in range(1, n-k+1): 
        boonja *= n
        n -= 1
    
    result.append(boonja//boonmo)

for r in result:
    print(r)
