import sys
from collections import deque

sys.stdin = open("section7/input/송아지_찾기.txt", "rt")

s, e = map(int, input().split())

MAX = 10000
dis = [0] * (MAX + 1)
visited = [False] * (MAX + 1)
dq = deque()
dq.append(s)

while dq:
    now = dq.popleft()
    if now == e:
        break
    for next in (now - 1, now + 1, now + 5):
        if (0 < next <= MAX) and (not visited[next]):
            dq.append(next)
            visited[next] = True
            dis[next] = dis[now] + 1

print(dis[e])
