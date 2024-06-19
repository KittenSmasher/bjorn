# https://codeforces.com/problemset/problem/791/A

a, b = map(int, input().split())

y = 0
while a < b+1:
    a *= 3
    b *= 2
    y += 1
    
print(y)