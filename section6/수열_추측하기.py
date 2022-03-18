import sys

sys.stdin = open("section6/input/수열_추측하기.txt", "rt")

def dfs(level, total):
    global switch
    if switch == True:
        return
    if (level == n) and (total == f):
        switch = True
        for x in seq:
            print(x, end = ' ')
    else:
        for i in range(1, n + 1):
            if used[i] == False:
                used[i] = True
                seq[level] = i
                dfs(level + 1, total + (seq[level] * b[level]))
                used[i] = False

n, f = map(int, input().split())

used = [False] * (n + 1)
seq = [0] * n
b = [1] * n
switch = False

for i in range(1, n):
    b[i] = b[i - 1] * (n - i) // i

dfs(0, 0)

# sol 2: 라이브러리를 이용한 순열
'''
import itertools as it

b = [1] * n
nums = list(range(1, n + 1))

for i in range(1, n):
    b[i] = b[i - 1] * (n - i) // i

for p in it.permutations(nums):
    total = 0
    for idx, x in enumerate(p):
        total += (x * b[idx])
    if total == f:
        for x in p:
            print(x, end = ' ')
        break
'''
