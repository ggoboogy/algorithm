x = int(input())

current = [64]
total = 64
while total > x:
    min_len = min(current)
    min_idx = current.index(min_len)
    half = min_len/2
    del current[min_idx]
    total -= min_len

    if half + total >= x:
        current.append(half)
        total += half
    else:
        current.append(half)
        current.append(half)
        total += half*2

print(len(current))
