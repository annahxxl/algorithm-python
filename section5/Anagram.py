import sys
from collections import Counter

sys.stdin = open("section5/input/Anagram.txt", "rt")

a = input()
b = input()

# sol 1
str = dict()

for x in a:
    str[x] = str.get(x, 0) + 1

for x in b:
    str[x] = str.get(x, 0) - 1

for x in a:
    if str[x] != 0:
        print('NO')
        break
else:
    print('YES')

# sol 2
'''
res = Counter(a) - Counter(b)

if len(res) == 0:
    print('YES')
else:
    print('NO')
'''

# sol 3: 파이썬에서 딕셔너리와 리스트는 == 과 != 연산이 가능하다.

# sol 4(리스트를 이용한 풀이 - ASCII 사용)\
'''
str1 = [0] * 52
str2 = [0] * 52

for x in a:
    if x.isupper():
        str1[ord(x) - 65] += 1
    else:
        str1[ord(x) - 71] += 1

for x in b:
    if x.isupper():
        str2[ord(x) - 65] += 1
    else:
        str2[ord(x) - 71] += 1

for i in range(52):
    if str1[i] != str2[i]:
        print('NO')
        break
else:
    print('YES')
'''
