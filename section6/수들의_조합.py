import sys

sys.stdin = open("section6/input/수들의_조합.txt", "rt")

def dfs(level, start, total):
    global cnt
    if level == k:
        if (total % m) == 0:
            cnt += 1
    else:
        for i in range(start, n):
            dfs(level + 1, i + 1, total + nums[i])

n, k = map(int, input().split())
nums = list(map(int, input().split()))
m = int(input())

cnt = 0

dfs(0, 0, 0)

print(cnt)

# sol 2: 라이브러리를 이용한 조합
'''
import itertools as it

cnt = 0

for c in it.combinations(nums, k):
    if (sum(c) % m) == 0:
        cnt += 1

print(cnt)
'''
