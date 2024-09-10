# https://codeforces.com/problemset/problem/344/A

n = int(input())

m = []

for _ in range(n):
    s = input().strip()
    m.append(s)

count = 1
for i in range(0, len(m)-1):
    if m[i] == m[i+1]:
        count += 0
    else:
        count += 1

print(count)
    