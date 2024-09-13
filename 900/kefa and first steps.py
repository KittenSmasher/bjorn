# https://codeforces.com/problemset/problem/580/A

n = int(input())

a = list(map(int, input().split()))

m = 1
x = 1

for i in range(1, n):
    if a[i] >= a[i-1]:
        m += 1
    else:
        x = max(x, m)
        m = 1

xx = max(x, m)       
print(xx)

