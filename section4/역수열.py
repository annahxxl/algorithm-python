import sys

sys.stdin = open("section4/input/역수열.txt", "rt")

n = int(input())
nums = list(map(int, input().split()))

# sol 1
'''
seq = [0] * n

for i in range(n):
    for j in range(n):
        if (nums[i] == 0) and (seq[j] == 0):
            seq[j] = i + 1
            break
        elif seq[j] == 0:
            nums[i] -= 1
'''

# sol 2
seq = []

nums = nums[::-1]

for i in nums:
        seq.insert(i, n)
        n -= 1

# 출력
for x in seq:
    print(x, end = ' ')
