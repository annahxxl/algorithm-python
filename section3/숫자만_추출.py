import sys

sys.stdin = open("section3/input/숫자만_추출.txt", "rt")

num_str = ''
cnt = 2;

for s in input():
    if s.isdigit():
        num_str += s

num = int(num_str)

for i in range(2, num):
    if num % i == 0:
        cnt += 1

print(num)
print(cnt)
