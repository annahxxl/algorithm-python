import sys

sys.stdin = open("section4/input/랜선자르기.txt", "rt")

def count(len):
    cnt = 0
    for line in lines:
        cnt += (line // len)
    return cnt

k, n = map(int, input().split())
lines = list(int(input()) for _ in range(k))

lp = 1
rp = max(lines)
maximum = 0

while lp <= rp:
    mid = (lp + rp) // 2
    if count(mid) >= n:
        maximum = mid
        lp = mid + 1
    else:
        rp = mid - 1

print(maximum)
