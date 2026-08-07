from collections import deque

N = int(input())
dq = deque([])

for _ in range(N):
    inputs = list(map(str, input().split()))

    if inputs[0] == 'push':
        dq.append(int(inputs[1]))
    if inputs[0] == 'pop':
        print(dq.popleft())
    if inputs[0] == 'size':
        print(len(dq))
    if inputs[0] == 'empty':
        print(1) if len(dq) == 0 else print(0)
    if inputs[0] == 'front':
        print(dq[0])


