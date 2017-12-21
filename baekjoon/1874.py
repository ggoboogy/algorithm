n = int(input())
stack = []
result = []
current = 1

for k in range(1, n+1):
    num = int(input())
    
    if len(stack) != 0 and stack[len(stack)-1] == num:
        del stack[len(stack)-1]
        result.append('-')
        continue

    for i in range(current, num+1):
        stack.append(i)
        result.append('+')

    del stack[len(stack)-1]
    result.append('-')
    current = num+1

if len(stack) != 0:
    print("NO")
else:
    for r in result:
        print(r)
