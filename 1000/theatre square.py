# https://codeforces.com/problemset/problem/1/A

import math
n, m, a = map(int, input().split())

x = math.ceil(n/a)
y = math.ceil(m/a)

print(x*y)