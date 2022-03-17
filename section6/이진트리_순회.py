import sys

sys.stdin = open("section6/input/이진트리_순회.txt", "rt")

def dfs(v):
    if v > 7:
        return
    else:
        # print(v, end = ' ') # 전위순회 출력 
        dfs(v * 2)
        # print(v, end = ' ') # 중위순회 출력
        dfs(v * 2 + 1)
        # print(v, end = ' ') # 후위순회 출력

dfs(1)
