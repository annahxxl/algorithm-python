import sys

sys.stdin = open("section6/input/중복순열_구하기.txt", "rt")

def dfs(level):
    global cnt
    if level == m:
        cnt += 1
        for i in res:
            print(i, end = ' ')
        print()
    else:
        for i in range(1, n + 1):
            res[level] = i
            dfs(level + 1)

n, m = map(int, input().split())

res = [0] * m
cnt = 0

dfs(0)

print(cnt)
