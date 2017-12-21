import operator
import sys

n = int(sys.stdin.readline())
result = {}
total = 0

for k in range(0, n):
    num = int(sys.stdin.readline())
    total += num

    if result.get(num) is None:
        result[num] = 1
    else:
        result[num] += 1

sorted_result = sorted(result.items(), key=operator.itemgetter(0))
tmp_list = list(result)
mid_val = tmp_list[int((len(tmp_list) - 1)/2)]
max_val = max(result)
min_val = min(result)
large1 = max(result.items(), key=operator.itemgetter(1))[0]
tmp_val = max(result.items(), key=operator.itemgetter(1))[1]
del result[large1]
large2 = max(result.items(), key=operator.itemgetter(1))[0]



print(round(total/n))
print(mid_val)
if result[large2] == tmp_val:
    print(large2)
else:
    print(large1)
print(max_val - min_val)
