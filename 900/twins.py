# https://codeforces.com/problemset/problem/160/A

n = int(input())

a = list(map(int, input().split()))

a = sorted(a)[::-1]

total = sum(a)
sumz = 0
cnt = 0

for i in a:
    sumz += i
    cnt += 1
    
    if sumz > total//2:
        break
    

print(cnt)
    
    