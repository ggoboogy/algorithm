import sys
tmp_a, tmp_b = sys.stdin.readline().split()
a = int(tmp_a)
b = int(tmp_b)

num1 = int('1'*a)
num2 = int('1'*b)

tmp = min(num1, num2)
result = str(tmp)
while int(result) > 0:
    if num1%int(result) == 0 and num2%int(result) == 0:
        break

    result = result[:len(result)-1]
print(result)
