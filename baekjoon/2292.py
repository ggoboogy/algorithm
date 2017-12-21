n = int(input())

init_num = 1
cnt = 1
while init_num < n:
    init_num += 6*cnt
    cnt+=1

print(cnt)
