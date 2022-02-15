import sys

sys.stdin = open("section2/input/정다면체.txt", "rt")

n, m = map(int, input().split())

cnt = [0] * (n + m + 1)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        cnt[i + j] += 1
maximum = max(cnt)
for i in range(len(cnt)):
    if cnt[i] == maximum:
        print(i, end = ' ')
