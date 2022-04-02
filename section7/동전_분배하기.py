import sys

sys.stdin = open("section7/input/동전_분배하기.txt", "rt")

def dfs(level):
    global res
    if level == n:
        diff = max(money) - min(money)
        if (diff < res) and (len(set(money)) == 3):
            res = diff
    else:
        for i in range(3):
            money[i] += coins[level]
            dfs(level + 1)
            money[i] -= coins[level]
    

n = int(input())
coins = list(int(input()) for _ in range(n))

money = [0] * 3
res = 2147000000

dfs(0)

print(res)
