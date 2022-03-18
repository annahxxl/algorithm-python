import sys

sys.stdin = open("section6/input/인접행렬.txt", "rt")

n, m = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j], end = ' ')
    print()
