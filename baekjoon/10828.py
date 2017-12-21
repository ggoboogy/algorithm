n = int(input())
result = []
stack = []

for k in range(0, n):
    tmp = input().split()
    inst = tmp[0]

    if inst == 'push':
        stack.append(int(tmp[1]))
    elif inst == 'pop':
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[len(stack)-1])
            del stack[len(stack)-1]
    elif inst == 'size':
        result.append(len(stack))
    elif inst == 'empty':
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)
    elif inst == 'top':
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[len(stack)-1])

for r in result:
    print(r)
