import sys

sys.stdin = open("section6/input/동전교환.txt", "rt")

def dfs(level, cur_sum):
    global res
    if level > res:
        return
    if cur_sum > m:
        return
    if cur_sum == m:
        if level < res:
            res = level
    else:
        for i in range(n):
            dfs(level + 1, cur_sum + coins[i])

n = int(input())
coins = list(map(int, input().split()))
m = int(input())

coins.sort(reverse = True)
res = 2147000000

dfs(0, 0)

print(res)
