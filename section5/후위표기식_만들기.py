import sys

sys.stdin = open("section5/input/후위표기식_만들기.txt", "rt")

ex = input()

stack = []
res = ''

for x in ex:
    if x.isdecimal():
        res += x
    else:
        if x == '(':
            stack.append(x)
        elif (x == '*') or (x == '/'):
            while stack and ((stack[-1] == '*') or (stack[-1] == '/')):
                res += stack.pop()
            stack.append(x)
        elif (x == '+') or (x == '-'):
            while stack and (stack[-1] != '('):
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and (stack[-1] != '('):
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()

print(res)
