n = int(input())
result = []

for k in range(0, n):
    tmp = input()
    stack = []

    for t in tmp:
        if t == '(':
            stack.append('(')
        elif t == ')':
            if len(stack) == 0:
                stack.append(')')
            else:
                if stack[len(stack)-1] == '(':
                    del stack[len(stack)-1]
                else:
                    stack.append(')')
        
    if len(stack) == 0:
        result.append('YES')
    else:
        result.append('NO')

for r in result:
    print(r)
