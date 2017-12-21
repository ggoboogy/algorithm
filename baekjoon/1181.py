n = int(input())
result = [[] for i in range(0, 51)]

for k in range(0, n):
    word = input()
    if word not in result[len(word)]:
        result[len(word)].append(word)

for i in range(1, 51):
    result[i].sort()
    for r in result[i]:
        print(r)
