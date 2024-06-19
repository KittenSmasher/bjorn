# https://codeforces.com/problemset/problem/637/A

from collections import Counter
t = int(input())

a = list(map(int, input().split()))

b = sorted(a)

cnt = Counter(b)

print(cnt)