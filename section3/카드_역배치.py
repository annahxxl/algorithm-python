import sys

sys.stdin = open("section3/input/카드_역배치.txt", "rt")

arr = list(range(21))

for _ in range(10):
    s, e = map(int, input().split())
    arr[s : e + 1] = reversed(arr[s : e + 1])

for i in range(1, 21):
    print(arr[i], end = ' ')
