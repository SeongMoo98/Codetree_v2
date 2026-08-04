N = int(input())
arr = list(map(int, input().split()))

for i in range(1, N):
    j = i-1
    value = arr[i]
    while j >= 0 and arr[j] > value:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = value


[print(x, end=' ') for x in arr]