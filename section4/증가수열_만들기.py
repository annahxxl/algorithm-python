import sys

sys.stdin = open("section4/input/증가수열_만들기.txt", "rt")

n = int(input())
nums = list(map(int, input().split()))

lp = 0
rp = n - 1
last = 0
tmp = []
res = ''

while lp <= rp:
    if nums[lp] > last:
        tmp.append((nums[lp], 'L'))
    if nums[rp] > last:
        tmp.append((nums[rp], 'R'))
    if len(tmp) == 0:
        break
    else:
        tmp.sort()
        last = tmp[0][0]
        res = res + tmp[0][1]
        if tmp[0][1] == 'L':
            lp += 1
        else:
            rp -= 1
    tmp.clear()

print(len(res))
print(res)
