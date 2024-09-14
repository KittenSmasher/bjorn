# https://codeforces.com/problemset/problem/112/A

x = input().upper()
y = input().upper()

if x < y:
    print(-1)
elif x > y:
    print(1)
else:
    print(0)

