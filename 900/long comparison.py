# https://codeforces.com/problemset/problem/1613/A

t = int(input())

def add_zero(x, p):
    x = str(x)
    res = x.ljust(p + len(x), '0')
    return int(res)
    
for _ in range(t):
    inp1 = list(map(int, input().split()))
    inp2 = list(map(int, input().split()))
    
    x1 = add_zero(inp1[0], inp1[1])
    x2 = add_zero(inp2[0], inp2[1])
    
    if (x1 < x2):
        print('<')
    elif(x1 > x2):
        print('>')
    elif(x1 == x2):
        print('=')
    
