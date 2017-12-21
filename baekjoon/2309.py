import sys
from itertools import permutations

num = [0 for i in range(0, 9)]
for i in range(0, 9):
    tmp = int(sys.stdin.readline())
    num[i] = tmp

per = permutations(num, 7)
for r in list(per):
    if sum(r) == 100:
        r = sorted(r)
        for i in r:
            print(i)
        break
