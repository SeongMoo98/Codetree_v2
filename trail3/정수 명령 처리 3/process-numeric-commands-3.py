from collections import deque

N = int(input())

q = deque([])

for _ in range(N):
    inputs = list(map(str,input().split()))

    if len(inputs) > 1 :
        inputs[1] = int(inputs[1])
        
    if inputs[0] == 'push_front':
        q.appendleft(inputs[1])
    if inputs[0] == 'push_back':
        q.append(inputs[1])
    if inputs[0] == 'pop_front':
        print(q.popleft())
    if inputs[0] == 'pop_back':
        print(q.pop())
    if inputs[0] == 'size':
        print(len(q))
    if inputs[0] == 'empty':
        print(1 if len(q) == 0 else 0)
    if inputs[0] == 'front':
        print(q[0])
    if inputs[0] == 'back':
        print(q[-1])
