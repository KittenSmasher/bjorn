# https://codeforces.com/problemset/problem/59/A

s = input()

low = 0
upp = 0

for i in s:
    if i.islower():
        low += 1
    else:
        upp += 1
        
if low < upp:
    s = s.upper()
else:
    s = s.lower()
    
print(s)