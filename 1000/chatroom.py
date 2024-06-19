# https://codeforces.com/problemset/problem/58/A

s = input()

helo = 'hello'

idx = 0

for c in s:
    print(idx)
    if idx < len(helo) and c == helo[idx]:
        idx += 1
    print(idx)

if idx == len(helo):
    print('YES')
else:
    print('NO')