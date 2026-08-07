N = int(input())
arr = []

for _ in range(N):
    inputs = list(map(str, input().split()))

    if inputs[0] == 'push':
        arr.append(int(inputs[1]))
    if inputs[0] == 'pop':
        print(arr.pop())
    if inputs[0] == 'size':
        print(len(arr))
    if inputs[0] == 'empty':
        print(1) if len(arr) == 0 else print(0)
    if inputs[0] == 'top':
        print(int(arr[-1]))
        




