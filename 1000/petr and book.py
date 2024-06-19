# https://codeforces.com/problemset/problem/139/A

n = int(input())

w = list(map(int, input().split()))

sum = 0
day = 0
while sum < n:
    sum += w[day]
    day = (day+1)%7

if day != 0:
    print(day)
else:
    print(7)