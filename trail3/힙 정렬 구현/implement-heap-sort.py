import heapq

N = int(input())
arr = list(map(int, input().split()))

heapq.heapify(arr)

for _ in range(N):
    print(heapq.heappop(arr), end=' ')
