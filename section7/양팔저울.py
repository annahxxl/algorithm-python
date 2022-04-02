import sys

sys.stdin = open("section7/input/양팔저울.txt", "rt")

def dfs(level, total):
    global res
    if level == k:
        if 0 < total <= weights_sum:
            res.add(total)
    else:
        dfs(level + 1, total + weights[level])
        dfs(level + 1, total - weights[level])
        dfs(level + 1, total)

k = int(input())
weights = list(map(int, input().split()))

weights_sum = sum(weights)
res = set()

dfs(0, 0)

print(weights_sum - len(res))
