import sys

sys.stdin = open("section7/input/알파코드.txt", "rt")

def dfs(idx1, idx2):
    global cnt
    if idx1 == n:
        cnt += 1
        for i in range(idx2):
            print(chr(res[i] + 64), end = '')
        print()
    else:
        for i in range(1, 27):
            if code[idx1] == i:
                res[idx2] = i
                dfs(idx1 + 1, idx2 + 1)
            elif (i >= 10) and (code[idx1] == (i // 10)) and (code[idx1 + 1] == (i % 10)):
                res[idx2] = i
                dfs(idx1 + 2, idx2 + 1)

code = list(map(int, input()))

cnt = 0
n = len(code)
code.append(-1)
res = [0] * n

dfs(0, 0)

print(cnt)
