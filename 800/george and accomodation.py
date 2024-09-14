# https://codeforces.com/problemset/problem/467/A

n = int(input())

cnt = 0

for _ in range(n):
    p, q = map(int, input().split())
    
    if p+2 <= q:
        cnt += 1

print(cnt)