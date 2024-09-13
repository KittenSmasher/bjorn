# https://codeforces.com/problemset/problem/479/A

a = int(input())
b = int(input())
c = int(input())

e = []

e.append(a+b+c)
e.append((a+b)*c)
e.append(a*(b+c))
e.append(a*b+c)
e.append(a+b*c)
e.append(a*b*c)

print(max(e))