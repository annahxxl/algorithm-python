import sys

sys.stdin = open("section4/input/씨름_선수.txt", "rt")

n = int(input())
players = list(tuple(map(int, input().split())) for _ in range(n))

players.sort(reverse=True)

maximum_height = 0
cnt = 0

for weight, height in players:
    if height > maximum_height:
        maximum_height = height
        cnt += 1

print(cnt)
