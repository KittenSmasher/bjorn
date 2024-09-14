# https://codeforces.com/problemset/problem/116/A

n = int(input())

p = 0
pp = []
for _ in range(n):
    a, b = map(int, input().split())
    p -= a
    p += b
    pp.append(p)
    
print(max(pp))
    