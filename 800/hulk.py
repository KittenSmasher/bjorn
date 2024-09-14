# https://codeforces.com/problemset/problem/705/A

n = int(input())

f = []

for i in range(1, n+1):
    if i%2==1:
        f.append("I hate")
    else:
        f.append("I love")

print(" that ".join(f) + " it")



