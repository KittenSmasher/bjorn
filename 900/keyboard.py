# https://codeforces.com/problemset/problem/474/A

# qwertyuiop
# asdfghjkl;
# zxcvbnm,./

w = 'qwertyuiopasdfghjkl;zxcvbnm,./'
n = input()
s = input()
res = []
if n == 'R':
    for i in s:
        res.append(w[w.index(i)-1])
else:
    for i in s:
        res.append(w[w.index(i)+1])
        
res = ''.join(res)

print(res)



