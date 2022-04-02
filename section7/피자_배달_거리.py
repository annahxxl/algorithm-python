import sys

sys.stdin = open("section7/input/피자_배달_거리.txt", "rt")

def dfs(level, start):
    global res
    if level == m:
        total = 0
        for i in range(len(house)):
            x1, y1 = house[i]
            dis = 2147000000
            for j in cb:
                x2, y2 = pizza[j]
                dis = min(dis, abs(x1 - x2) + abs(y1 - y2))
            total += dis
        res = min(res, total)
    else:
        for i in range(start, len(pizza)):
            cb[level] = i
            dfs(level + 1, i + 1)

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

house = []
pizza = []
cb = [0] * m
res = 2147000000
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            pizza.append((i, j))

dfs(0, 0)

print(res)
