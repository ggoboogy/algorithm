import sys

n = int(sys.stdin.readline())
num1 = 0
num2 = 1
num3 = 0
for i in range(2, n+1):
    num3 = num1 + num2
    num1 = num2
    num2 = num3

print(num3%1000000)
