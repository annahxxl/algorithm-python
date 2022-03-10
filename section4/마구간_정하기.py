import sys

sys.stdin = open("section4/input/마구간_정하기.txt", "rt")

def count(dis):
    cnt = 1
    start = loc[0]
    for i in range(1, n):
        if (loc[i] - start) >= dis:
            cnt += 1
            start = loc[i]
    return cnt

n, c = map(int, input().split())
loc = list(int(input()) for _ in range(n))

loc.sort()

lp = 1
rp = loc[-1]
maximum = 0

while lp <= rp:
    mid = (lp + rp) // 2
    if count(mid) >= c:
        maximum = mid
        lp = mid + 1
    else:
        rp = mid - 1

print(maximum)
