import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
tmp = sys.stdin.readline().split()
m_list = [int(tmp[i]) for i in range(0, m)]

str_n = str(n)
result = ""
for i in range(0, len(str_n)):
    min_val = 10
    min_k = 0
    for k in range(0, 10):
        if k not in m_list and abs(k-int(str_n[i])) < min_val:
            min_val = abs(k-int(str_n[i]))
            min_k = k

    result += str(min_k)

cnt = len(result) + abs(int(result)-n)
print(min(abs(100-int(n)),cnt))
