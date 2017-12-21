place_num = int(input())
tmp = input()
person = tmp.split()
b, c = input().split()

total = 0

for k in range(0, place_num):
    left = int(person[k]) - int(b)
    if left < 0: tmp1 = 1
    elif left%int(c) == 0: tmp1 = 1 + (left/int(c))
    else: tmp1 = 1 + (left/int(c)) + 1

    total += int(tmp1)

print(total)
