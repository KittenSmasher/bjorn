# https://codeforces.com/problemset/problem/208/A


s = input().strip()

s = s.split('WUB')

while '' in s:
    s.remove('')     

print(' '.join(s))