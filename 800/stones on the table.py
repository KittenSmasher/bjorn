# https://codeforces.com/problemset/problem/266/A

n = int(input())
inp = input().strip()

r = 0

for i in range(1, n):
    if inp[i] == inp[i-1]:
        r += 1

print(r)