# https://codeforces.com/problemset/problem/996/A

n = int(input())

b = 0

b = n//100
r = n%100

b += r//20
r = r%20

b += r//10
r = r%10

b += r//5
r = r%5

b += r//1
print(b)