# https://codeforces.com/problemset/problem/598/A

t = int(input())

for _ in range(t):
    n = int(input())
    
    # S(n) = (n * (n+1)) // 2
    total_sum = n * (n+1) // 2
    
    sum_power = 0
    power = 1
    
    while sum_power <= n:
        sum_power += power
        power *= 2
    
    result = total_sum - 2 * sum_power
    
    print(result)
