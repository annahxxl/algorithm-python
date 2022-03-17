import sys

sys.stdin = open("section6/input/부분집합_구하기.txt", "rt")

def dfs(v):
    if v == (n + 1):
        for i in range(1, n + 1):
            if used[i] == True:
                print(i, end = ' ')
        print()
    else:
        used[v] = True
        dfs(v + 1)
        used[v] = False
        dfs(v + 1)

n = int(input())

used = [False] * (n + 1)

dfs(1)
