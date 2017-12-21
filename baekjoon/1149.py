n = int(input())
table = [[] for i in range(0, n)]

for i in range(0, n):
    tmp_r, tmp_g, tmp_b = input().split()
    table[i].append(int(tmp_r))
    table[i].append(int(tmp_g))
    table[i].append(int(tmp_b))

dp = [[] for i in range(0, n)]
current = n - 1
while current >= 0:
    if current == n - 1:
        dp[current] = table[current]
    else:
        tmp_list = dp[current+1]
        min1 = min(tmp_list)
        min1_idx = dp[current+1].index(min1)
        del tmp_list[min1_idx]
        min2 = min(tmp_list)
        min2_idx = dp[current+1].index(min2)
        for k in range(0, 3):
            if k == min1_idx:
                dp[current].append(table[current][k] + min2)
            else:
                dp[current].append(table[current][k] + min1)

    current -= 1

print(min(dp[0]))
