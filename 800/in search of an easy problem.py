# https://codeforces.com/problemset/problem/1030/A

n = int(input())

s = map(int, input().split())

if sum(s) == 0:
    print('EASY')
else:
    print('HARD')