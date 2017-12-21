t = int(input())
result = []

for i in range(0, t):
    p = input()
    n = int(input())
    tmp = input()
    tmp = tmp.replace('[', '')
    tmp = tmp.replace(']', '')
    num = tmp.split(',')
    
    err_flag = 0
    cnt = 0
    for j in range(0, len(p)):
        if p[j] == 'R':
            cnt += 1

        elif p[j] == 'D':
            if n == 0:
                err_flag = 1
                break
            else:
                if cnt%2 == 0:
                    num.remove(num[0])
                else:
                    num.remove(num[n-1])
                n -= 1
    if err_flag:
        result.append("error")
    elif len(num) == 0:
        result.append("[]")
    else:
        tmp = "["
        if cnt%2 == 1:
            for i in range(0, n-1):
                tmp += num[n-i-1] + ","
            tmp += num[0]
        else:
            for i in range(0, n-1):
                tmp += num[i] + ","
            tmp += num[n-1]
        tmp += "]"
        result.append(tmp)

for r in result:
    print(r)
