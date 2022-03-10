import sys

sys.stdin = open("section4/input/회의실_배정.txt", "rt")

n = int(input())
meetings = list(tuple(map(int, input().split())) for _ in range(n))

meetings.sort(key=lambda x : (x[1], x[0]))

end_time = 0
cnt = 0

for start, end in meetings:
    if start >= end_time:
        end_time = end
        cnt += 1
    
print(cnt)
