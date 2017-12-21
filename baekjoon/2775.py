t = int(input())

data = [[0]*15 for i in range(15)]
for k in range(0, 15):
    for i in range(1, 15):
        if k == 0 or i == 1:
            data[k][i] = i
        else:
            data[k][i] = data[k][i-1] + data[k-1][i]

result = []

for i in range(0, t):
    k = int(input())
    n = int(input())

    result.append(data[k][n])

for k in range(0, t):
    print(result[k])

