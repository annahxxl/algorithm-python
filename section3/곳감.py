import sys

sys.stdin = open("section3/input/곳감.txt", "rt")

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
for _ in range(int(input())):
    row, dir, size = map(int, input().split())

    if dir == 0:
        for _ in range(size):
            grid[row - 1].append(grid[row - 1].pop(0))
    else:
        for _ in range(size):
            grid[row - 1].insert(0, grid[row - 1].pop())

    s = 0
    e = n - 1
    cnt = 0

    for i in range(n):
        cnt += sum(grid[i][s : e + 1])
        if i < n // 2:
            s += 1
            e -= 1
        else:
            s -= 1
            e += 1

print(cnt)
