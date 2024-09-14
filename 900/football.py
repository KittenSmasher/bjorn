# https://codeforces.com/problemset/problem/96/A

s = input()

c0 = 0
c1 = 0
for c in s:
    if c == '1':
        c1 += 1
        if c1 == 7:
            break
        c0 = 0
    elif c == '0':  
        c0 += 1
        if c0 == 7:
            break
        c1 = 0

if c0 >= 7 or c1 >= 7:
    print('YES')
else:
    print('NO')