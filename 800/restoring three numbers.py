# https://codeforces.com/problemset/problem/1154/A

x1, x2, x3, x4 = map(int, input().split())

s = [x1, x2, x3, x4]

s = sorted(s)

s[0] = x1
s[1] = x2
s[2] = x3
s[3] = x4

a = x1+x2-x3
b = (x1-x2+x3)//2
c = x3-x1

print(a, b, c)

