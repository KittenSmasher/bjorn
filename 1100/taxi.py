# https://codeforces.com/contest/158/problem/B
from collections import Counter

n = int(input())
s = list(map(int, input().split()))

cnt = Counter(s)

taxi = 0

# group of 4 one taxi
taxi += cnt[4]

# group of 3 one taxi + one person
taxi += cnt[3]
cnt[1] = max(0, cnt[1]-cnt[3])

# 2 group of 2 one taxi
taxi += cnt[2] // 2
if cnt[2] % 2:
    taxi += 1
    cnt[1] = max(0, cnt[1]-2)

taxi += (cnt[1] + 3) // 4

print(taxi)