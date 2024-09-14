# https://codeforces.com/problemset/problem/1955/A

t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())
    
    if a*2 < b:
        res = n*a
    else:     
        promo = n // 2 * b
        no_promo = n % 2 * a   
        res = promo+no_promo 
    
    print(res)