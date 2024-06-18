# https://codeforces.com/problemset/problem/1512/A

from collections import Counter
t = int(input())

for i in range(t):
    n = int(input())
    
    a = list(map(int, input().split()))
    
    cnt = Counter(a)
    
    for x in cnt:
        if cnt[x] == 1:
            print(a.index(x) + 1)
    