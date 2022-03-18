import sys

sys.stdin = open("section6/input/조합_구하기.txt", "rt")

# sol 1
def dfs(level, start):
    global cnt
    if level == m:
        cnt += 1
        for i in range(m):
            print(res[i], end = ' ')
        print()
    else:
        for i in range(start, n + 1):
            res[level] = i
            dfs(level + 1, i + 1) # 중복 조합을 구하고 싶을 경우 dfs(level + 1, i)로 호출한다.

n, m = map(int, input().split())

res = [0] * (m + 1)
cnt = 0

dfs(0, 1)

print(cnt)
