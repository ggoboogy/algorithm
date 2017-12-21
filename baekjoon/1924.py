x, y = input().split()
m = int(x)
d = int(y)

day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
result = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

total = 0

for i in range(0, m-1):
    total += day[i]

total += d

print(result[total%7])
