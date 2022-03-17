import sys

sys.stdin = open("section6/input/합이_같은_부분집합.txt", "rt")

def dfs(level, cur_sum):
    global switch
    if cur_sum > nums_sum // 2:
        return
    if level == n:
        if cur_sum == (nums_sum - cur_sum):
            switch = True
            return
    else:
        dfs(level + 1, cur_sum + nums[level])
        dfs(level + 1, cur_sum)

n = int(input())
nums = list(map(int, input().split()))

nums_sum = sum(nums)
switch = False

dfs(0, 0)

if switch:
    print('YES')
else:
    print('NO')
