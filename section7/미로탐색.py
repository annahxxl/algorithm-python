import sys

sys.stdin = open("section7/input/미로탐색.txt", "rt")

def dfs(x, y):
    global cnt
    if (x == 6) and (y == 6):
        cnt += 1
    else:
        for i in range(4):
            nx, ny = x + direction[i][0], y + direction[i][1]
            if (0 <= nx < 7) and (0 <= ny < 7) and maze[nx][ny] == 0:
                maze[nx][ny] = 1
                dfs(nx, ny)
                maze[nx][ny] = 0

maze = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
maze[0][0] = 1
direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]

dfs(0, 0)

print(cnt)
