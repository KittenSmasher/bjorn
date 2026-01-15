# https://codeforces.com/problemset/problem/1676/A


t = int(input())

for i in range(t):
    s = input() 
      
    a = s[0:3]
    b = s[-3:]
    
    aa = []
    bb = []
    
    for x in a:
        aa.append(int(x))
    
    for y in b:
        bb.append(int(y))
       
    if(sum(aa) == sum(bb)):
        print("YES")
    else:
        print("NO")
    
