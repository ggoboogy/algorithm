n = input()
result = [-1 for i in range(0, 10)]

for s in n:
    if result[int(s)] == -1:
        result[int(s)] = 1
    else:
        result[int(s)] += 1

current = 9
while current >= 0:
    if result[current] != -1:
        for j in range(0, result[current]):
            print(current, end='')
    current -= 1
print()
