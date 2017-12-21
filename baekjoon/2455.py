import sys

max_num = 0
person = 0
for i in range(0, 4):
    tmp_out, tmp_in = sys.stdin.readline().split()
    out = int(tmp_out)
    in_num = int(tmp_in)

    person = person - out + in_num
    if person > max_num:
        max_num = person

print(max_num)
