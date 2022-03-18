import sys

sys.stdin = open("section6/input/순열_구하기.txt", "rt")

def dfs(level):
    global cnt
    if level == m:
        cnt += 1
        for i in range(m):
            print(res[i], end = ' ')
        print()
    else:
        for i in range(1, n + 1):
            if used[i] == False:
                used[i] = True
                res[level] = i
                dfs(level + 1)
                used[i] = False

n, m = map(int, input().split())

used = [False] * (n + 1)
res = [0] * m
cnt = 0

dfs(0)

print(cnt)
