import sys

sys.stdin = open("section3/input/회문_문자열_검사.txt", "rt")

for i in range(int(input())):
    s = input().upper()
    if s == s[::-1]:
        print('#{0} YES'.format(i + 1))
    else:
        print('#{0} NO'.format(i + 1))
