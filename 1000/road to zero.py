# https://codeforces.com/problemset/problem/1342/A\
    
t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    a, b = map(int, input().split())

    costA = a * abs(max(x,y)-min(x,y))
    costB = b * min(abs(x), abs(y))
    
    print(costA+costB)
    
