import sys

sys.stdin = open("section2/input/K번째_큰_수.txt", "rt")

n, k = map(int, input().split())
cards = list(map(int, input().split()))

sums = set()
for i in range(n):
    for j in range(i + 1, n):
        for t in range(j + 1, n):
            sums.add(cards[i] + cards[j] + cards[t])
sums = sorted(sums, reverse=True)

print(sums[k - 1])
