import sys

sys.stdin = open("section5/input/후위식_연산.txt", "rt")

ex = input()

stack = []

for x in ex:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(b + a)
        elif x == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif x == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(b * a)
        elif x == '/':
            a = stack.pop()
            b = stack.pop()
            stack.append(b / a)

print(stack[0])
