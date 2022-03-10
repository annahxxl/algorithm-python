import sys

sys.stdin = open("section4/input/뮤직비디오.txt", "rt")

def count(capacity):
    cnt = 1
    total = 0
    for music in musics:
        if (total + music) > capacity:
            cnt += 1
            total = music
        else:
            total += music
    return cnt

n, m = map(int, input().split())
musics = list(map(int, input().split()))

lp = 1
rp = sum(musics)
minimum = 0
max_music = max(musics)

while lp <= rp:
    mid = (lp + rp) // 2
    if (mid >= max_music) and (count(mid) <= m):
        minimum = mid
        rp = mid - 1
    else:
        lp = mid + 1

print(minimum)
