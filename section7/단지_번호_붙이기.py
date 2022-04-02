import sys

sys.stdin = open("section7/input/단지_번호_붙이기.txt", "rt")

def dfs(x, y):
    global cnt
    cnt += 1
    map[x][y] = 0
    for i in range(4):
        nx, ny = x + direction[i][0], y + direction[i][1]
        if (0 <= nx < n) and (0 <= ny < n) and (map[nx][ny] == 1):
            dfs(nx, ny)

n = int(input())
map = [list(map(int, input())) for _ in range(n)]

res = []
direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]

for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            cnt = 0
            dfs(i, j)
            res.append(cnt)
            
res.sort()

print(len(res))
for x in res:
    print(x)
