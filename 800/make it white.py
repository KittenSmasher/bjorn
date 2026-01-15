# https://codeforces.com/problemset/problem/1927/A

t = int(input())

for _ in range(t):
    n = int(input())
    
    s = input()
    b = []
    
    for x in range(len(s)):
        if s[x] == 'B':
            b.append(x)
            
    a = b[len(b)-1]
    c = b[0]
            
    print(a-c+1)



    