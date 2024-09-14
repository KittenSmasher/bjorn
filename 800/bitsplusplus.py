# https://codeforces.com/problemset/problem/282/A

n = int(input())

x = 0
for _ in range(n):
    z = input()
    
    if '++' in z:
        x += 1
    elif '--' in z:
        x -= 1

print(x)
        