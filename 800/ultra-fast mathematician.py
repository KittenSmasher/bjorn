# https://codeforces.com/problemset/problem/61/A

x = input()
y = input()

res = []

for i in range(len(x)):
    if x[i] == y[i]:
        r = '0'
    else:
        r = '1'
    res.append(r)

res = ''.join(res)
print(res)