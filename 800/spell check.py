# https://codeforces.com/problemset/problem/1722/A

t = int(input())
tt = 'Timur'

for _ in range(t):
    n = int(input())
    s = input()

    cnt = 0
    
    for x in s:
        if x in tt:
            cnt += 1

    if cnt == 5:
        print('yes')
    else:
        print('NO')

