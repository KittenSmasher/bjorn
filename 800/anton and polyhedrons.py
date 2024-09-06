# https://codeforces.com/problemset/problem/785/A

poly = {
    "Tetrahedron" : 4,
    "Cube" : 6,
    "Octahedron" : 8,
    "Dodecahedron" : 12,
    "Icosahedron" : 20
}

n = int(input())

arr = []

for _ in range(n):
    s = input()
    arr.append(poly[s])
    
print(sum(arr))