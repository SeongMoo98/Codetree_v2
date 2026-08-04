N = int(input())
arr = list(map(int, input().split()))

for i in range(N-1):
    for j in range(N-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

[print(x, end=' ') for x in arr]

