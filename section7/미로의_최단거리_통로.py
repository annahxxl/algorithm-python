import sys
from collections import deque

sys.stdin = open("section7/input/미로의_최단거리_통로.txt", "rt")

maze = [list(map(int, input().split())) for _ in range(7)]

dis = [[0] * 7 for _ in range(7)]
dq = deque()
dq.append((0, 0))
maze[0][0] = 1
direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]

while dq:
    x, y = dq.popleft()
    for i in range(4):
        nx, ny = x + direction[i][0], y + direction[i][1]
        if (0 <= nx < 7) and (0 <= ny < 7) and (maze[nx][ny] == 0):
            dis[nx][ny] = dis[x][y] + 1
            maze[nx][ny] = 1
            dq.append((nx, ny))
        
if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])
    