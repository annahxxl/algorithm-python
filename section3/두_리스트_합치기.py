import sys

sys.stdin = open("section3/input/두_리스트_합치기.txt", "rt")

n = int(input())
nums1 = list(map(int, input().split()))
m = int(input())
nums2 = list(map(int, input().split()))

p1 = p2 = 0
answer = []

while (p1 < n) and (p2 < m):
    if nums1[p1] <= nums2[p2]:
        answer.append(nums1[p1])
        p1 += 1
    else:
        answer.append(nums2[p2])
        p2 += 1
if p1 < n:
    answer += nums1[p1:]
if p2 < m:
    answer += nums2[p2:]

for x in answer:
    print(x, end = ' ')
