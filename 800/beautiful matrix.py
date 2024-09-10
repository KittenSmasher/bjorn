# https://codeforces.com/problemset/problem/263/A

matrix = []

for i in range(5):
    row = input()
    matrix.append([int(x) for x in row.split()])

step = 0
center = len(matrix) // 2
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            step = abs(i-center) + abs(j-center)

print(step)