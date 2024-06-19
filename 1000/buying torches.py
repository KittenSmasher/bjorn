# https://codeforces.com/problemset/problem/1418/A
import math
t = int(input())

for _ in range(t):
    x, y, k = map(int, input().split())
    
    # craft k torch need k coal and k stick
    sticks = k * (y+1)
    stick = sticks-1
    trade = (stick+x-2)//(x-1)
    
    total_trade = trade+k
    
    print(total_trade)
    
    