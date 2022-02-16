import sys

sys.stdin = open("section2/input/자릿수의_합.txt", "rt")

def digit_sum(x):
    return sum(map(int, str(x)))

n = int(input())
nums = list(input().split())

maximum = 0
answer = 0

for num in nums:
    total = digit_sum(num)
    if total > maximum:
        maximum = total
        answer = num

print(answer)
