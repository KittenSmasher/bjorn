# https://codeforces.com/problemset/problem/69/A

n = int(input())

xx = []
yy = []
zz = []

for _ in range(n):
    x, y, z = map(int, input().split())
    xx.append(x)
    yy.append(y)
    zz.append(z)

x = sum(xx)
y = sum(yy)
z = sum(zz)

if x == 0 and y == 0 and z == 0:
    print('YES')
else:
    print('NO')