# https://codeforces.com/problemset/problem/230/A

s, n = map(int, input().split())

dragons = []

for _ in range(n):
    x, y = map(int, input().split())
    dragons.append((x,y))

dragons.sort()

can = False

for d in dragons:
    x, y = d
    
    if s > x:
        s += y
        can = True
    else:
        can = False
        
if can:
    print('YES')
else:
    print('NO')
        