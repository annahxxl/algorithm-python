import sys

sys.stdin = open("section7/input/안전영역.txt", "rt")

def dfs(x, y, height):
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + direction[i][0], y + direction[i][1]
        if (0 <= nx < n) and (0 <= ny < n) and (not visited[nx][ny]) and (area[nx][ny] > height):
            dfs(nx, ny, height)

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

res = 0
direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]

for height in range(100):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (not visited[i][j]) and (area[i][j] > height):
                cnt += 1
                dfs(i, j, height)
    res = max(res, cnt)
    if cnt == 0:
        break

print(res)
