import sys

sys.stdin = open("section3/input/격자판_최대합.txt", "rt")

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

row = 0
col = 0
x = 0

for i in range(n):
    row = max(sum(grid[i]), row)
    tmp = 0
    for j in range(n):
        tmp += grid[j][i]
    col = max(tmp, col)

left, right = 0, 0

for i in range(n):
    left += grid[i][i]
    right += grid[n - 1 - i][n - 1 - i]
    if i == (n - 1):
        x = max(left, right)

print(max(row, col, x))
