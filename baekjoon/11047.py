n, k = input().split()
N = int(n)
K = int(k)
value_list = []

for idx in range(0, N):
    value = int(input())
    if value <= K:
        value_list.append(value)

rest = K
total = 0
while rest != 0:
    last_idx = len(value_list) -1
    if value_list[last_idx] > rest:
        del value_list[last_idx]
    else:
        mok = int(rest/value_list[last_idx])
        total += mok
        rest -= mok*value_list[last_idx]

print(total)
