n = input()
result = [0,1,2,3,4,5,6,7,8,9]
cnt = 1

for tmp in n:
    s = int(tmp)
    if s in result:
        result.remove(s)
    else:
        if s == 6 and 9 in result:
            result.remove(9)
            continue
        if s == 9 and 6 in result:
            result.remove(6)
            continue

        cnt += 1
        for i in range(0,10):
            result.append(i)
        result.remove(s)

print(cnt)
