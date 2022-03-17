import sys

sys.stdin = open("section6/input/재귀함수를_이용한_이진수_출력.txt", "rt")

def dfs(n):
    if n == 0:
        return
    else:
        dfs(n // 2)
        print(n % 2, end = '')

n = int(input())

dfs(n)
