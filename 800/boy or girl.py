# https://codeforces.com/problemset/problem/236/A

from collections import Counter
inp = str(input())

cnt = Counter(inp)

n = len(cnt)

if n % 2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")
