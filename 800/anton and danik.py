# https://codeforces.com/problemset/problem/734/A

from collections import Counter

n = int(input())

s = input()

cnt = Counter(s)

if cnt['A'] > cnt['D']:
    print('Anton')
elif cnt['A'] < cnt['D']:
    print('Danik')
else:
    print('Friendship')
 