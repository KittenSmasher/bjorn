# https://codeforces.com/problemset/problem/617/A

n = int(input())

if n <= 5:
    print(1)
else:
    step = n // 5
    sisa = n % 5

    if  0 < sisa <= 5:
        step = step+1

    print(step)