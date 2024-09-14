# https://codeforces.com/problemset/problem/1829/A

n = int(input())

for _ in range(n): 
    s = input()
    c = 'codeforces'
    cnt = 0

    for i,z in enumerate(s):
        if z != c[i]:
            cnt += 1

    print(cnt)

