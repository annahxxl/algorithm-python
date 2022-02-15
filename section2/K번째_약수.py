import sys

sys.stdin = open("section2/input/K번째_약수.txt", "rt")

n, k = map(int, input().split())

divisors = []
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
    if len(divisors) == k:
        print(i)
        break
else:
    print(-1)
