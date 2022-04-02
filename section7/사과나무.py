import sys
from collections import deque

sys.stdin = open("section7/input/사과나무.txt", "rt")

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
cnt = 0
dq = deque()
mid = n // 2
dq.append((mid, mid))
visited[mid][mid] = True
cnt += grid[mid][mid]
level = 0
direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]

while level < mid:
    for i in range(len(dq)):
        x, y = dq.popleft()
        for i in range(4):
            nx, ny = x + direction[i][0], y + direction[i][1]
            if not visited[nx][ny]:
                cnt += grid[nx][ny]
                visited[nx][ny] = True
                dq.append((nx, ny))
    level += 1

print(cnt)
