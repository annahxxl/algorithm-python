import sys

sys.stdin = open("section2/input/주사위_게임.txt", "rt")

n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]

rewards = []

for a, b, c in dices:
    if (a == b) and (b == c):
        rewards.append(10000 + a * 1000)
    elif (a == b) or (a == c):
        rewards.append(1000 + a * 100)
    elif b == c:
        rewards.append(1000 + b * 100)
    else:
        rewards.append(max(a, b, c) * 100)

print(max(rewards))
