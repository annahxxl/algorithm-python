import sys
from collections import deque

sys.stdin = open("section5/input/교육과정_설계.txt", "rt")

needs = input()
print(needs)

for i in range(int(input())):
    plan = input()
    dq = deque(needs)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print('#{0} NO'.format(i + 1))
                break
    else:
        if len(dq) == 0:
            print('#{0} YES'.format(i + 1))
        else:
            print('#{0} NO'.format(i + 1))

    