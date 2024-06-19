# https://codeforces.com/problemset/problem/122/A

n = input().strip()

def lucky(n):
    for char in str(n):
        if char != '4' and char != '7':
            return False
    return True

factors = [i for i in range(1, int(n)+1) if int(n) % i == 0 and lucky(i)]
# print(factors)
cnt = {'4': n.count('4'), '7': n.count('7')}

if factors or cnt['4'] + cnt['7'] == len(n):
    print('YES')
else:
    print('NO')