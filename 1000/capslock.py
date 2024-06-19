# https://codeforces.com/problemset/problem/131/A

s = input()

if s.isupper():
    s = s.lower()
    
elif len(s) == 1 and s.lower():
    s = s.upper()
    
elif s[0].islower() and s[1:].isupper():
    s = s[0].upper() + s[1:].lower() 
    
print(s)
