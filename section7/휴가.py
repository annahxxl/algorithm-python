import sys

sys.stdin = open("section7/input/휴가.txt", "rt")

def dfs(day, money):
    global res
    if day == n + 1:
        if money > res:
            res = money
    else:
        if (day + m[day][0]) <= (n + 1):
            dfs(day + m[day][0], money + m[day][1])
        dfs(day + 1, money)

n = int(input())
m = list(tuple(map(int, input().split())) for _ in range(n))

m.insert(0, (0, 0))
res = 0

dfs(1, 0)

print(res)
