import sys

sys.stdin = open("section5/input/가장_큰_수.txt", "rt")

n, m = map(int, input().split())

n = list(map(int, str(n)))

stack = []

for x in n:
    while stack and (m > 0) and (stack[-1] < x):
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:
    stack = stack[:-m]

print(int(''.join(map(str, stack))))
