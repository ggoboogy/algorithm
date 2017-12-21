n, m = input().split()
N = int(n)
M = int(m)

queue = []
result = []

for k in range(1, N+1):
    queue.append(k)

start_idx = 0
while len(queue) > 0:
    cal = (start_idx + M - 1) % len(queue)
    result.append(queue[cal])
    del queue[cal]
    start_idx = cal

print("<", end='')
for k in result:
    print(k, end='')
    if result.index(k) != len(result)-1:
        print(", ", end='')
print(">")
