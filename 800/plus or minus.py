# https://codeforces.com/problemset/problem/1807/A

t = int(input())

for i in range(t):
    res = False
    s = list(map(int, input().split()))
    
    plus = s[0] + s[1]
    minus = s[0] - s[1]
    
    if(plus == s[2]):
        print('+')
    elif(minus == s[2]):
        print('-')