n = int(input())
yang = [2000 for i in range(1001)]
um = [2000 for i in range(1001)]

for k in range(0, n):
    num = int(input())
    if num < 0:
        um[abs(num)] = num
    else:
        yang[num] = num

current = 1000
while current != 0:
    if um[current] != 2000:
        print(um[current])
    current -= 1

for r in yang:
    if r != 2000:
        print(r)
