t = int(input())
result = []

for k in range(0, t):
    tmp_n, tmp_m = input().split()
    priority = input().split()
    n = int(tmp_n)
    m = int(tmp_m)
    out_list = []

    while len(out_list) != n:
        if priority[0] == max(priority):
            out_list.append(priority[0])
            del priority[0]

            if m == 0:
                result.append(len(out_list))
                break
            else:
                m -= 1
        else:
            tmp = priority[0]
            del priority[0]
            priority.append(tmp)

            if m == 0:
                m = len(priority) - 1
            else:
                m -= 1

for r in result:
    print(r)
