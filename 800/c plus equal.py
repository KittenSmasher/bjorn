# https://codeforces.com/problemset/problem/1368/A

t = int(input())


for _ in range(t):
    a, b, n = map(int, input().split())
    cnt = 0
    
    while a < n+1:
        if a > b:
            x = a
            a = b
            b = x

        a += b
        cnt += 1
        
    print(cnt)
    
    
    