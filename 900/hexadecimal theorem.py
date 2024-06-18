# https://codeforces.com/problemset/problem/199/A

n = int(input())

a, b = 0, 1
fib = []

fib.append(a)

while b <= n:
    fib.append(b)
    a, b = b, a+b
    
res = []

for i in range(len(fib)):
    for j in range(len(fib)):
        for k in range(len(fib)):
            if (fib[i]+fib[j]+fib[k] == n):
                res.append((fib[i], fib[j], fib[k]))

res = res[0]
print(f"{res[0]} {res[1]} {res[2]}")
            





