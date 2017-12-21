import math

t = int(input())
result = []

for k in range(0, t):
    tmp1, tmp2, tmp3 = input().split()
    h = int(tmp1)
    w = int(tmp2)
    n = int(tmp3)

    num = math.ceil(n/h)
    floor = n - (h*(num-1))
    
    new_n = format(num, '02')
    result.append(str(floor)+str(new_n))

for r in result:
    print(r)
