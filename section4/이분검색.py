import sys

sys.stdin = open("section4/input/이분검색.txt", "rt")

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

lp = 0
rp = n - 1

while lp <= rp:
    mid = (lp + rp) // 2
    if m == nums[mid]:
        print(mid + 1)
        break
    elif m < nums[mid]:
        rp = mid - 1
    else:
        lp = mid + 1
