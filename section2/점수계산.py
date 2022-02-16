import sys

sys.stdin = open("section2/input/점수계산.txt", "rt")

n = int(input())
result = list(map(int, input().split()))

score = 0
continuous = 0

for r in result:
    if r == 1:
        continuous += 1
        score += continuous
    else:
        continuous = 0

print(score)
