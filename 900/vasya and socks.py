# https://codeforces.com/problemset/problem/460/A

n, m = map(int, input().split())

day = 0

while n > 0:
    n -= 1
    day += 1
    
    
    if day % m == 0:
        n += 1
    
    
print(day)
        

