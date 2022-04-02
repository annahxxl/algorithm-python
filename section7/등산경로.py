import sys

sys.stdin = open("section7/input/등산경로.txt", "rt")

def dfs(x, y):
    global cnt
    if (x == ex) and (y == ey):
        cnt += 1
    else:
        for i in range(4):
            nx, ny = x + direction[i][0], y + direction[i][1]
            if (0 <= nx < n) and (0 <= ny < n) and (not visited[nx][ny]) and (mountain[nx][ny] > mountain[x][y]):
                visited[nx][ny] = True
                dfs(nx, ny)
                visited[nx][ny] = False

n = int(input())
mountain = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
maximum = -2147000000
minimum = 2147000000
for i in range(n):
    for j in range(n):
        if mountain[i][j] < minimum:
            minimum = mountain[i][j]
            sx, sy = i, j
        if mountain[i][j] > maximum:
            maximum = mountain[i][j]
            ex, ey = i, j
visited[sx][sy] = True
cnt = 0
direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]

dfs(sx, sy)

print(cnt)
