# https://codeforces.com/problemset/problem/118/A

s = input()

vowel = ['a', 'o', 'y', 'e', 'u', 'i']

s = s.lower()

res = ['.'+c for c in s if c not in vowel]

res = ''.join(res)

print(res)
