# https://codeforces.com/problemset/problem/677/A

n, h = map(int, input().split())

p = list(map(int, input().split()))

sum = 0

for i in p:
    if i > h:
        sum += 2
    else:
        sum += 1
        
print(sum)