# https://codeforces.com/problemset/problem/1294/A

t = int(input())

for _ in range(t):
    a, b, c, n = map(int, input().split())
    
    m = max(a,b,c)
    
    x = (m-a) + (m-b) + (m-c)
    
    if x > n:
        print('NO')
    elif (n-x) % 3 == 0:
        print('YES')
    else:
        print('NO')
    


