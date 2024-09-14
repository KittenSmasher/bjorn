# https://codeforces.com/problemset/problem/405/A

n = int(input())

s = list(map(int, input().split()))

s = sorted(s)

print(' '.join(map(str, s)))