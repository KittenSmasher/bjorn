# https://codeforces.com/problemset/problem/581/A

a, b = map(int, input().split())

x = 0
y = 0

if a <= b:
    x = a
else:
    x = b

y = ((a-x) + (b-x)) // 2
print(x, y)
