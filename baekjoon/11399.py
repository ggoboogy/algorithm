n = int(input())
tmp_list = input().split()
p_list = []

for k in range(0, n):
    p_list.append(int(tmp_list[k]))

sorted_list = []
total = 0
num = n

sorted_list = sorted(p_list)

for i in range(0, n):
    total += int(sorted_list[i])*num
    num -= 1

print(total)
