import sys
from collections import deque

sys.stdin = open("section7/input/섬나라_아일랜드.txt", "rt")

n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
dq = deque()
direction = [(0, -1), (-1, 0), (0, 1), (1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]

for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            map[i][j] = 0
            dq.append((i, j))
            while dq:
                x, y = dq.popleft()
                for k in range(8):
                    nx, ny = x + direction[k][0], y + direction[k][1]
                    if (0 <= nx < n) and (0 <= ny < n) and (map[nx][ny] == 1):
                        map[nx][ny] = 0
                        dq.append((nx, ny))
            cnt += 1

print(cnt)
