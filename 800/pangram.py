# https://codeforces.com/problemset/problem/520/A

import re

n = int(input())
s =input()

x = re.compile(r'[a-z]', re.IGNORECASE)
found = set(x.findall(s.lower()))

if len(found) == 26:
    print("YES")
else:
    print("NO")


