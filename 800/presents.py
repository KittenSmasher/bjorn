# https://codeforces.com/problemset/problem/136/A

n = int(input())

p = list(map(int, input().split()))

nn = []

for i in range(1, n+1):
    nn.append(i)
    
x = list(zip(p, nn))
xx = sorted(x)

res = [i[1] for i in xx]

print(' '.join(map(str, res)))
