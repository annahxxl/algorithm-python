import sys
from collections import deque

sys.stdin = open("section5/input/공주_구하기.txt", "rt")

n, k = map(int, input().split())

circle = deque(range(1, n + 1))

while circle:
    for _ in range(k - 1):
        circle.append(circle.popleft())
    circle.popleft()
    if len(circle) == 1:
        print(circle.pop())
