# https://codeforces.com/problemset/problem/271/A

inp =  input().strip()

while True:
    inp = str(int(inp) + 1) 
    
    if len(set(inp)) == 4:
        print(inp)
        break