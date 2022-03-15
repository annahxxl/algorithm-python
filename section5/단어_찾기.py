import sys

sys.stdin = open("section5/input/단어_찾기.txt", "rt")

n = int(input())

poem = dict()

for i in range(n):
    word = input()
    poem[word] = poem.get(word, 0) + 1

for i in range(n - 1):
    word = input()
    poem[word] -= 1

for key, val in poem.items():
    if val == 1:
        print(key)
        break
