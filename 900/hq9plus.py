# https://codeforces.com/problemset/problem/133/A

h = ['H', 'Q', '9']

p = input()
f = False
for i in p:
    if i in h:
        f = True
        break
    else:
        f = False

if f:
    print('YES')
else:
    print('NO')