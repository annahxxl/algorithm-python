import sys
from collections import deque

sys.stdin = open("section7/input/토마토.txt", "rt")

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

dq = deque()
dis = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            dq.append((i, j))
direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]

while dq:
    x, y = dq.popleft()
    for i in range(4):
        nx, ny = x + direction[i][0], y + direction[i][1]
        if (0 <= nx < n) and (0 <= ny < m) and (box[nx][ny] == 0):
            box[nx][ny] = 1
            dis[nx][ny] = dis[x][y] + 1
            dq.append((nx, ny))

every = True

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            every = False

res = 0

if every:
    for i in range(n):
        for j in range(m):
            res = max(res, dis[i][j])
    print(res)
else:
    print(-1)
