deque = []
n = int(input())

result = []
for i in range(0, n):
    cmd = input().split()

    if cmd[0] == "push_front": deque.insert(0,cmd[1])

    elif cmd[0] == "push_back": deque.append(cmd[1])

    elif cmd[0] == "pop_front":
        if len(deque) == 0: result.append(-1)
        else:
            result.append(deque[0])
            deque.remove(deque[0])

    elif cmd[0] == "pop_back":
        if len(deque) == 0: result.append(-1)
        else: result.append(deque.pop())
    
    elif cmd[0] == "size": result.append(len(deque))

    elif cmd[0] == "empty":
        if len(deque) == 0: result.append(1)
        else:result.append(0)

    elif cmd[0] == "front":
        if len(deque) == 0: result.append(-1)
        else: result.append(deque[0])

    elif cmd[0] == "back":
        if len(deque) == 0: result.append(-1)
        else: result.append(deque[len(deque)-1])

for r in result:
    print(r)
