import sys

sys.stdin = open("section7/input/최대점수_구하기.txt", "rt")

def dfs(level, score, time):
    global res
    if time > m:
        return
    if level == n:
        if score > res:
            res = score
    else:
        dfs(level + 1, score + p[level][0], time + p[level][1])
        dfs(level + 1, score, time)

n, m = map(int, input().split())
p = list(tuple(map(int, input().split())) for _ in range(n))

res = 0

dfs(0, 0, 0)

print(res)
