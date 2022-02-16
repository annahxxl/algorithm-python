import sys

sys.stdin = open("section2/input/소수.txt", "rt")

n = int(input())

check = [True] * (n + 1)
cnt = 0

for i in range(2, n + 1):
    if check[i] == True:
        cnt += 1
    for j in range(i, n + 1, i):
        check[j] = False

print(cnt)
