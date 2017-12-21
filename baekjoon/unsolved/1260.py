tmp_n, tmp_m, tmp_v = input().split()

n = int(tmp_n)
m = int(tmp_m)
v = int(tmp_v)
table = [[] for k in range(0, n+1)]

for k in range(0, m):
    tmp_x, tmp_y = input().split()
    x = int(tmp_x)
    y = int(tmp_y)

    table[x].append(y)
    table[y].append(x)

dfs = []
current = v
while True:
    if len(table[current]) == 0 or current in dfs:
        break
    else:
        dfs.append(current)
        
        for node in table[current]:
            if node not in dfs:
                current = node
                break
print(dfs)

bfs = [v]
current = v
while True:
    for node in table[current]:
        if node not in bfs:
            bfs.append(node)
    if current + 1 == n:
        current = 0
    else:
        current += 1

    if current == v:
        break
print(bfs)
