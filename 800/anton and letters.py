# https://codeforces.com/problemset/problem/443/A

from collections import Counter
inp = input()

e = list(inp.strip('{}').split(', '))
# print(e)
if e == ['']:
    print(0)
else:
    print(len(Counter(e)))