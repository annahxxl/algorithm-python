import sys

sys.stdin = open("section2/input/K번째_수.txt", "rt")

for i in range(int(input())):
    n, s, e, k = map(int, input().split())
    nums = list(map(int, input().split()))
    
    nums = sorted(nums[s - 1 : e])

    print('#{0} {1}'.format(i + 1, nums[k - 1]))
