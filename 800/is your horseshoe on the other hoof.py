# https://codeforces.com/problemset/problem/228/A

from collections import Counter
s = list(map(int, input().split()))

cnt = Counter(s)

shoes = 0

for i in cnt:
    if cnt[i] == 2:
        shoes += 1
    elif cnt[i] == 3:
        shoes += 2
    elif cnt[i] == 4:
        shoes += 3
    else:
        shoes += 0

print(shoes)