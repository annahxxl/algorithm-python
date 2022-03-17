import sys

sys.stdin = open("section6/input/바둑이_승차.txt", "rt")

def dfs(level, cur_sum, judged_sum):
    global res
    if cur_sum + (weights_sum - judged_sum) < res:
        return
    if cur_sum > c:
        return
    if level == n:
        if cur_sum > res:
            res = cur_sum
    else:
        dfs(level + 1, cur_sum + weights[level], judged_sum + weights[level])
        dfs(level + 1, cur_sum, judged_sum + weights[level])

c, n = map(int, input().split())
weights = list(int(input()) for _ in range(n))

res = 0
weights_sum = sum(weights)

dfs(0, 0, 0)

print(res)
