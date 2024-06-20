# https://codeforces.com/problemset/problem/1950/C

t = int(input())

for _ in range(t):
    s = input()

    h, m = s.split(':')
    
    h = int(h)

    if h > 12:
        h = abs(h-12)
        x = 'PM' 
    elif h == 12:
        x = 'PM'
    elif h == 0:
        h = abs(h-12)
        x = 'AM' 
    else:
        x = 'AM'
        
    if h < 10:
        h = str(h)
        h = '0'+h
        
    h = str(h)    
        
    time = h + ':' + m + ' ' + x
        
    print(time)
    