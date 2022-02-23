import sys

sys.stdin = open("section3/input/격자판_회문수.txt", "rt")

grid = [list(map(int, input().split())) for _ in range(7)]

cnt = 0

for i in range(3):
    for j in range(7):
        part = grid[j][i : (i + 5)]
        if part == part[::-1]:
            cnt += 1
        for k in range(2):
            if grid[i + k][j] != grid[i + 4 - k][j]:
                break
        else:
            cnt += 1

print(cnt)
