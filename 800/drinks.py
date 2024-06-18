# https://codeforces.com/problemset/problem/200/B

n = int(input())
p = list(map(int, input().split()))

s = []

for i in range(n):
    p[i] = p[i] / 100
    s.append(p[i])
     
sum = sum(s)

res = (sum/n)*100

print(float(res))
    