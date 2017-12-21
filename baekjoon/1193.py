n =  int(input())

x = 1
y = 1
flag = 1
for k in range(0, n-1):
    if flag == 1 and x == 1:
        y += 1
        flag = 0
    elif flag == 0 and y == 1:
        x += 1
        flag = 1
    else:
        if flag == 0:
            x += 1
            y -= 1
        else:
            x -= 1
            y += 1
    
print(str(x)+"/"+str(y))
