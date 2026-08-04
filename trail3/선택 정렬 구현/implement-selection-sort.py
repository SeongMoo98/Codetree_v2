N = int(input())
arr = list(map(int, input().split()))

for i in range(N):
    min = i
    for j in range(i+1, N):
        if arr[j] < arr[min]:
            min = j               
    temp = arr[min]
    arr[min] = arr[i]
    arr[i] = temp

[print(x, end=' ') for x in arr]  