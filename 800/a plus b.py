# https://codeforces.com/problemset/problem/1772/A

n = int(input())

for _ in range(n):
    s = input()
    
    if s[1] == '+':
        print(int(s[0]) + int(s[2]))
        
