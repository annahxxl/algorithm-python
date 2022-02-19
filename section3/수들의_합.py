import sys

sys.stdin = open("section3/input/수들의_합.txt", "rt")

n, m = map(int, input().split())
arr = list(map(int, input().split()))

lp = 0
rp = 1
total = arr[0]
cnt = 0;

while True:
    if total < m:
        if rp < n:
            total += arr[rp]
            rp += 1
        else:
            break
    elif total == m:
        cnt += 1
        total -= arr[lp]
        lp += 1
    else:
        total -= arr[lp]
        lp += 1

print(cnt)
