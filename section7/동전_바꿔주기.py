import sys

sys.stdin = open("section7/input/동전_바꿔주기.txt", "rt")

def dfs(level, total):
    global cnt
    if total > t:
        return
    if level == k:
        if total == t:
            cnt += 1
    else:
        for i in range(coins[level][1] + 1):
            dfs(level + 1, total + (coins[level][0] * i))

t = int(input())
k = int(input())
coins = list(tuple(map(int, input().split())) for _ in range(k))

cnt = 0

dfs(0, 0)

print(cnt)
