import sys

sys.stdin = open("section2/input/대표값.txt", "rt")

n = int(input())
scores = list(map(int, input().split()))

# 파이썬에서 round 메서드는 round_half_even 방식을 택하고 있다.
# → round_half_even? 정확하게 .5 로 떨어질 경우 짝수 쪽으로 값을 지정해 주는 것
# avg = round(sum(scores) / n + 0.5)
# 그래서 위에 코드를 아래와 같이 수정해 준다.
avg = int(sum(scores) / n + 0.5)
min_diff = 100
score = 0
number = 0
for idx, value in enumerate(scores):
    diff = abs(avg - value)
    if diff < min_diff:
        min_diff = diff
        score = value
        number = idx + 1
    elif diff == min_diff:
        if value > score:
            score = value
            number = idx + 1

print(avg, number)
