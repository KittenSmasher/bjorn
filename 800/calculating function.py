# https://codeforces.com/problemset/problem/486/A

inp = int(input())

def f(n):
    if n % 2 == 0:
            return n // 2
    else:
        return -(n + 1) // 2
    
print(f(inp))

