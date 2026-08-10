import heapq

N = int(input())
arr = [0] + list(map(int, input().split()))

def heapify(N, i):
    largest = i
    left = 2 * i
    right = 2 * i + 1

    if left <= N and arr[left] > arr[largest]:
        largest = left
    if right <= N and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(N, largest)


def heap_sort():
    for i in range(N//2, 0, -1):
        heapify(N, i)

    for i in range(N, 1, -1):
        arr[1], arr[i] = arr[i], arr[1]
        heapify(i-1, 1)


heap_sort()

for x in arr[1:]:
    print(x, end=' ')