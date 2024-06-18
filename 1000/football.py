# https://codeforces.com/problemset/problem/43/A

from collections import Counter
t = int(input())

goals = []

for _ in range(t):
    n = input()
    goals.append(n)
    
team = Counter(goals)
 
win = max(team, key=team.get)
 
print(win)

