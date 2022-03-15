import sys
from collections import deque

sys.stdin = open("section5/input/응급실.txt", "rt")

n, m = map(int, input().split())
patients = deque((pos, val) for pos, val in enumerate(list(map(int, input().split()))))

cnt = 0

while True:
    cur = patients.popleft()
    if any(cur[1] < x[1] for x in patients):
        patients.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break
