N = int(input())

queue = []
inst = []

for k in range(0, N):
    inst.append(input().split())

for idx in range(0, N):
    if inst[idx][0] =="push":
        queue.append(inst[idx][1])
    
    elif inst[idx][0] == "pop":
        if len(queue) == 0: print("-1")
        else:
            print(queue[0])
            del queue[0]

    elif inst[idx][0] == "size":
        print(len(queue))

    elif inst[idx][0] == "empty":
        if len(queue) == 0: print("1")
        else: print("0")

    elif inst[idx][0] == "front":
        if len(queue) == 0: print("-1")
        else: print(queue[0])

    elif inst[idx][0] == "back":
        if len(queue) == 0: print("-1")
        else: print(queue[len(queue)-1])
