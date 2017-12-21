n = int(input())
time_table = []

for k in range(0, n):
    tmp1, tmp2 = input().split()
    tmp_arr = [int(tmp1), int(tmp2)]
    time_table.append(tmp_arr)

time_table.sort(key=lambda x: (x[0],x[1]))
print(time_table)


total = 1
last_time = 0

for i in range(0, n):
    if 

print(max_total)
"""
