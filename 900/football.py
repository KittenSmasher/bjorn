# https://codeforces.com/problemset/problem/96/A

s = input()

cnt = 0
curr = None
for i in s:
    if i == curr:
        cnt += 1
    else:
        curr == i
        cnt = 1

if cnt >= 7:
    print('YES')
else:
    print('NO')