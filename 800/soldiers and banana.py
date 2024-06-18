# https://codeforces.com/problemset/problem/546/A

k, n, w = (map(int, input().split()))

price = 0
for i in range(1, w+1):
    price += k*i

if(n < price):
    print(price-n)
else:
    print(0)

 