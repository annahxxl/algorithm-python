import sys

sys.stdin = open("section3/input/사과나무.txt", "rt")

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
s = e = mid = n // 2

for i in range(n):
    cnt += sum(grid[i][s : e + 1])
    if i < mid:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(cnt)
