import sys

sys.stdin = open("section2/input/뒤집은_소수.txt", "rt")

def reverse(x):
    x = str(x)
    return int(''.join(x[::-1]))

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, x // 2 + 1): # 1과 자기자신을 제외한 약수의 범위는 2 ~ n // 2 이다.
        if x % i == 0:
            return False
    return True

n = int(input())
nums = list(map(int, input().split()))

for num in nums:
    num = reverse(num)
    if is_prime(num):
        print(num, end = ' ')
