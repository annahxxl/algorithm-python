import sys

sys.stdin = open("section6/input/경로_탐색.txt", "rt")

def dfs(v):
    global cnt
    if v == n:
        cnt += 1
    else:
        for i in range(1, n + 1):
            if (graph[v][i] == 1) and (not visited[i]):
                visited[i] = True
                dfs(i)
                visited[i] = False

n, m = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

cnt = 0
visited = [False] * (n + 1)

visited[1] = True
dfs(1)

print(cnt)
