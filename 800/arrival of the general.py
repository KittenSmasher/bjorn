# https://codeforces.com/problemset/problem/144/A

n = int(input())

arr = list(map(int, input().split()))

swap = 0
for i in range(len(arr)-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            swap += 1
            arr[j], arr[j+1] = arr[j+1], arr[j]
            
            
            
print(swap)