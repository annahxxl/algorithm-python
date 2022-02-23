import sys

sys.stdin = open("section3/input/봉우리.txt", "rt")

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
grid.insert(0, [0] * n)
grid.append([0] * n)
for arr in grid:
    arr.insert(0, 0)
    arr.append(0)

cnt = 0
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if all(grid[i][j] > grid[i + dir[k][0]][j + dir[k][1]] for k in range(4)):
            cnt += 1

print(cnt)
