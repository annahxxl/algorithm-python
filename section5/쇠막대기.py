import sys

sys.stdin = open("section5/input/쇠막대기.txt", "rt")

ex = input()

stack = []
cnt = 0

for i in range(len(ex)):
    if ex[i] == '(':
        stack.append(ex[i])
    else:
        stack.pop()
        if ex[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)
